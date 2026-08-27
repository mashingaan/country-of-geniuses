$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$required = @(
  "README.md",
  "AGENTS.md",
  "LICENSE",
  "CONTRIBUTING.md",
  "SECURITY.md",
  "docs/trust-and-safety.md",
  "skills/civic-problem-triage/SKILL.md",
  "schemas/problem-card.schema.json",
  "examples/problem-card.example.json"
)

foreach ($relativePath in $required) {
  $absolutePath = Join-Path $root $relativePath
  if (-not (Test-Path -LiteralPath $absolutePath -PathType Leaf)) {
    throw "Missing required file: $relativePath"
  }
}

$schemaPath = Join-Path $root "schemas/problem-card.schema.json"
$examplePath = Join-Path $root "examples/problem-card.example.json"
$schema = Get-Content -Raw -LiteralPath $schemaPath | ConvertFrom-Json
$example = Get-Content -Raw -LiteralPath $examplePath | ConvertFrom-Json

if ($schema.'$schema' -ne "https://json-schema.org/draft/2020-12/schema") {
  throw "Unexpected JSON Schema draft"
}

if ($example.id -notmatch "^cog-[a-z0-9-]+$") {
  throw "Example id does not match the public problem-card convention"
}

if ($example.privacy.contains_personal_data -ne $false) {
  throw "Example must be explicitly marked as containing no personal data"
}

if ($example.privacy.redaction_reviewed -ne $true) {
  throw "Example must be explicitly marked as redaction reviewed"
}

if ($example.action.human_confirmation_required -ne $true) {
  throw "Example must require human confirmation"
}

Write-Output "Country of Geniuses repository checks passed"
