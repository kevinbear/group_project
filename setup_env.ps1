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

# Check pip Installation
if (Get-Command pip -ErrorAction SilentlyContinue) {
    Write-Host "✔ pip is installed: $(pip --version)" -ForegroundColor Green
} else {
    Write-Host "❌ pip is not found. Installing pip..."
    python -m ensurepip --default-pip
    if (Get-Command pip -ErrorAction SilentlyContinue) {
        Write-Host "✔ pip installed successfully!" -ForegroundColor Green
    } else {
        Write-Host "❌ pip installation failed. Please check your Python installation." -ForegroundColor Red
        exit
    }
}

# Check pyenv-win Installation
if (Get-Command pyenv -ErrorAction SilentlyContinue) {
    Write-Host "✔ pyenv-win is installed: $(pyenv --version)" -ForegroundColor Green
} else 
{
    Write-Host "❌ pyenv-win is not installed. Installing now..."
    Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "install-pyenv-win.ps1"
    & ".\install-pyenv-win.ps1"

    # Verify pyenv-win installation
    if (Get-Command pyenv -ErrorAction SilentlyContinue) 
    {
        Write-Host "✔ pyenv-win installed successfully!" -ForegroundColor Green
    } else {
        Write-Host "❌ pyenv-win installation failed. Please install manually from https://github.com/pyenv-win/pyenv-win" -ForegroundColor Red
        exit
    }
}

# Create Virtual Environment
Write-Host "Creating virtual environment (windows_dev_env)..." -ForegroundColor Cyan
python -m venv windows_dev_env
Write-Host "✔ Virtual environment created: windows_dev_env" -ForegroundColor Green

# Instructions to Activate Virtual Environment
Write-Host "To activate the virtual environment, run:" -ForegroundColor Yellow
Write-Host ".\windows_dev_env\Scripts\Activate.ps1" -ForegroundColor White

# Install Required Packages
Write-Host "Installing dependencies from requirements.txt..." -ForegroundColor Cyan
pip install -r requirements.txt
Write-Host "✔ All required packages installed!" -ForegroundColor Green

# Final Success Message
Write-Host "Windows environment setup completed successfully!" -ForegroundColor Green
