"""Durable storage for the ACECOG engine: one SQLite file per installation.

Local-first (spec 11.5): the authoritative record is a file on hardware the Civic Body
controls, and the system runs without a network connection.

What is stored, all append-only except the small bookkeeping tables:

    events    the hash-chained event log (11.3, ASR-04)
    versions  every immutable object version (DPP-IMMUTABLE-001)
    commands  the result of every command, keyed by command_id (idempotency, 8.1)
    actors    actor registry
    counters  identifier counters
    exports   completed export packages (ASR-11)

Each governed transaction is written in ONE SQLite transaction, so a command either
lands completely or not at all (8.1 atomicity). On open, the hash chain is verified
before the engine accepts any command; a broken chain refuses to start (tamper evidence).
"""
import json
import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS events   (seq INTEGER PRIMARY KEY, json TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS versions (oid TEXT NOT NULL, n INTEGER NOT NULL, json TEXT NOT NULL, PRIMARY KEY (oid, n));
CREATE TABLE IF NOT EXISTS commands (command_id TEXT PRIMARY KEY, json TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS actors   (actor_id TEXT PRIMARY KEY, json TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS counters (prefix TEXT PRIMARY KEY, n INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS exports  (export_id TEXT PRIMARY KEY, json TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS meta     (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TRIGGER IF NOT EXISTS events_no_update BEFORE UPDATE ON events BEGIN SELECT RAISE(ABORT, 'event log is append-only'); END;
CREATE TRIGGER IF NOT EXISTS events_no_delete BEFORE DELETE ON events BEGIN SELECT RAISE(ABORT, 'event log is append-only'); END;
CREATE TRIGGER IF NOT EXISTS versions_no_update BEFORE UPDATE ON versions BEGIN SELECT RAISE(ABORT, 'object versions are immutable'); END;
CREATE TRIGGER IF NOT EXISTS versions_no_delete BEFORE DELETE ON versions BEGIN SELECT RAISE(ABORT, 'object versions are immutable'); END;
"""
STORE_FORMAT = "acecog-store/1"


def dumps(o):
    return json.dumps(o, sort_keys=True, separators=(",", ":"), default=str)


class Store:
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(path, isolation_level=None, check_same_thread=False)
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("PRAGMA synchronous=FULL")
        self.db.executescript(SCHEMA)
        row = self.db.execute("SELECT value FROM meta WHERE key='format'").fetchone()
        if row is None:
            self.db.execute("INSERT INTO meta VALUES ('format', ?)", (STORE_FORMAT,))
        elif row[0] != STORE_FORMAT:
            raise RuntimeError(f"{path} is format {row[0]}, expected {STORE_FORMAT}")

    # ------------------------------------------------------------------ load
    def load(self):
        q = lambda sql: self.db.execute(sql).fetchall()
        versions = {}
        for oid, n, js in q("SELECT oid, n, json FROM versions ORDER BY oid, n"):
            versions.setdefault(oid, []).append(json.loads(js))
        return {
            "events": [json.loads(js) for (js,) in q("SELECT json FROM events ORDER BY seq")],
            "versions": versions,
            "commands": {k: json.loads(js) for k, js in q("SELECT command_id, json FROM commands")},
            "actors": {k: json.loads(js) for k, js in q("SELECT actor_id, json FROM actors")},
            "counters": dict(q("SELECT prefix, n FROM counters")),
            "exports": {k: json.loads(js) for k, js in q("SELECT export_id, json FROM exports")},
        }

    # ---------------------------------------------------------------- commit
    def commit(self, events, versions, command_id, result, actors, counters, exports):
        """Write one governed transaction atomically."""
        c = self.db
        c.execute("BEGIN IMMEDIATE")
        try:
            c.executemany("INSERT INTO events (seq, json) VALUES (?, ?)", [(e["seq"], dumps(e)) for e in events])
            c.executemany("INSERT INTO versions (oid, n, json) VALUES (?, ?, ?)", [(v["id"], int(v["version_id"].rsplit("@v", 1)[1]), dumps(v)) for v in versions])
            if command_id is not None:
                c.execute("INSERT INTO commands (command_id, json) VALUES (?, ?)", (command_id, dumps(result)))
            c.executemany("INSERT INTO actors (actor_id, json) VALUES (?, ?) ON CONFLICT(actor_id) DO UPDATE SET json=excluded.json",
                          [(k, dumps(v)) for k, v in actors.items()])
            c.executemany("INSERT INTO counters (prefix, n) VALUES (?, ?) ON CONFLICT(prefix) DO UPDATE SET n=excluded.n", list(counters.items()))
            c.executemany("INSERT INTO exports (export_id, json) VALUES (?, ?)", [(k, dumps(v)) for k, v in exports.items()])
            c.execute("COMMIT")
        except Exception:
            c.execute("ROLLBACK")
            raise

    def close(self):
        self.db.close()
