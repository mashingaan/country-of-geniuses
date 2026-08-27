$ErrorActionPreference = "Stop"

$pythonScript = Join-Path $PSScriptRoot "validate-repo.py"
& python $pythonScript @args
if ($LASTEXITCODE -ne 0) {
  exit $LASTEXITCODE
}
