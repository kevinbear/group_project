# Windows Setup Environment Script
# Run this script in PowerShell as Administrator

Write-Host "Checking Windows Development Environment..." -ForegroundColor Cyan

# Check Execution Policy
$executionPolicy = Get-ExecutionPolicy
if ($executionPolicy -eq "Restricted") {
    Write-Host "Execution policy is restricted. Temporarily allowing script execution..." -ForegroundColor Yellow
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
}

# Check Python Installation
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "✔ Python is installed: $(python --version)" -ForegroundColor Green
} else {
    Write-Host "❌ Python is not installed. Please install Python from https://www.python.org/downloads/" -ForegroundColor Red
    exit
}

# Set the RENDER environment variable
Write-Host "Setting environment variable RENDER='False'..." -ForegroundColor Cyan
[System.Environment]::SetEnvironmentVariable("RENDER", "False", [System.EnvironmentVariableTarget]::User)

# Verify the environment variable was set
$renderValue = [System.Environment]::GetEnvironmentVariable("RENDER", [System.EnvironmentVariableTarget]::User)
if ($renderValue -eq "False") {
    Write-Host "✔ Environment variable RENDER set successfully!" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to set environment variable RENDER." -ForegroundColor Red
}

# Apply changes to the current session
$env:RENDER = "False"

# Create Virtual Environment
Write-Host "Creating virtual environment (windows_dev_env)..." -ForegroundColor Cyan
python -m venv windows_dev_env
Write-Host "✔ Virtual environment created: windows_dev_env" -ForegroundColor Green

# Instructions to Activate Virtual Environment
Write-Host "To activate the virtual environment, run:" -ForegroundColor Yellow
Write-Host ".\windows_dev_env\Scripts\Activate.ps1" -ForegroundColor White

# Install Required Packages
Write-Host "Installing dependencies from requirements.txt..." -ForegroundColor Cyan
pip install --no-cache-dir -r requirements.txt
Write-Host "✔ All required packages installed!" -ForegroundColor Green

Write-Host "✅ Windows environment setup completed successfully!" -ForegroundColor Green