# Reset Windows Development Environment
# Run this script in PowerShell as Administrator

Write-Host "Resetting Windows Development Environment..." -ForegroundColor Cyan

# Remove RENDER environment variable
Write-Host "Removing environment variable RENDER..." -ForegroundColor Yellow
[System.Environment]::SetEnvironmentVariable("RENDER", $null, [System.EnvironmentVariableTarget]::User)

# Verify removal
$renderValue = [System.Environment]::GetEnvironmentVariable("RENDER", [System.EnvironmentVariableTarget]::User)
if ($null -eq $renderValue) {
    Write-Host "✔ Environment variable RENDER removed successfully!" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to remove environment variable RENDER." -ForegroundColor Red
}

# Remove virtual environment
$venvPath = ".\windows_dev_env"
if (Test-Path $venvPath) {
    Write-Host "Removing virtual environment (windows_dev_env)..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force $venvPath
    Write-Host "✔ Virtual environment removed successfully!" -ForegroundColor Green
} else {
    Write-Host "⚠ Virtual environment not found. Skipping..." -ForegroundColor Red
}

# Refresh PowerShell Environment
Write-Host "Refreshing PowerShell environment..." -ForegroundColor Cyan
$env:RENDER = $null
Write-Host "✔ Environment reset completed successfully!" -ForegroundColor Green

# Prompt user to restart PowerShell for full effect
Write-Host "⚠ Please restart PowerShell to apply changes fully." -ForegroundColor Yellow