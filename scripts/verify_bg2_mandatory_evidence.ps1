param([Parameter(Mandatory=$true)][string]$Archive,[Parameter(Mandatory=$true)][string]$ExpectedSha256)
$ErrorActionPreference='Stop'
if((Get-FileHash -LiteralPath $Archive -Algorithm SHA256).Hash.ToLowerInvariant() -cne $ExpectedSha256){throw 'Archive hash mismatch'}
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip=[IO.Compression.ZipFile]::OpenRead((Resolve-Path -LiteralPath $Archive))
try {
  $entries=@{}
  foreach($entry in $zip.Entries){
    if($entries.ContainsKey($entry.FullName) -or $entry.FullName -match '(^/|\\|:|(^|/)\.\.(/|$))'){throw 'Unsafe or duplicate entry'}
    $entries[$entry.FullName]=$entry
  }
  $s=$entries['SHA256SUMS'].Open(); $reader=[IO.StreamReader]::new($s)
  try {$lines=$reader.ReadToEnd() -split "`n"} finally {$reader.Dispose()}
  $expected=@{}
  foreach($line in $lines){if(!$line.Trim()){continue};if($line -notmatch '^([0-9a-f]{64})  (.+)$'){throw 'Invalid checksum line'};if($expected.ContainsKey($Matches[2])){throw 'Duplicate checksum'};$expected[$Matches[2]]=$Matches[1]}
  if($entries.Count -ne $expected.Count+1){throw 'Missing or extra member'}
  foreach($name in $expected.Keys){
    if(!$entries.ContainsKey($name)){throw "Missing member $name"}
    $stream=$entries[$name].Open();$h=[Security.Cryptography.SHA256]::Create()
    try {$actual=[Convert]::ToHexString($h.ComputeHash($stream)).ToLowerInvariant()}finally{$stream.Dispose();$h.Dispose()}
    if($actual -cne $expected[$name]){throw "Payload hash mismatch $name"}
  }
  $stream=$entries['index.html'].Open();$reader=[IO.StreamReader]::new($stream)
  try {$html=$reader.ReadToEnd()} finally {$reader.Dispose()}
  $links=[regex]::Matches($html,'href="([^"]+)"');foreach($link in $links){if(!$entries.ContainsKey($link.Groups[1].Value)){throw 'Dangling local link'}}
  Write-Output "PASS: $($entries.Count) unique archive entries; $($expected.Count) payload hashes; $($links.Count) local links; exact archive digest. Independent QA and human legal review remain separate."
} finally {$zip.Dispose()}
