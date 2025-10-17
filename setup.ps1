# Google Maps Scraper - Setup Script
# Run this script to set up the project

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Google Maps Scraper - Setup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check Python version
Write-Host "Checking Python version..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "✗ Python not found. Please install Python 3.10 or higher." -ForegroundColor Red
    exit 1
}

# Create virtual environment
Write-Host ""
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
} else {
    python -m venv venv
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Virtual environment created" -ForegroundColor Green
    } else {
        Write-Host "✗ Failed to create virtual environment" -ForegroundColor Red
        exit 1
    }
}

# Activate virtual environment
Write-Host ""
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host ""
Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt --quiet --disable-pip-version-check
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Python dependencies installed" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to install dependencies" -ForegroundColor Red
    exit 1
}

# Install Playwright browsers
Write-Host ""
Write-Host "Installing Playwright browsers..." -ForegroundColor Yellow
Write-Host "This may take a few minutes..." -ForegroundColor Gray
playwright install chromium
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Playwright browsers installed" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to install Playwright browsers" -ForegroundColor Red
    exit 1
}

# Create necessary directories
Write-Host ""
Write-Host "Verifying directory structure..." -ForegroundColor Yellow
$directories = @("output", "logs", "config")
foreach ($dir in $directories) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
    }
}
Write-Host "✓ Directory structure verified" -ForegroundColor Green

# Setup complete
Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "✓ Setup Complete!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To run the application:" -ForegroundColor Yellow
Write-Host "  1. Activate the virtual environment: .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "  2. Run the application: python main.py" -ForegroundColor White
Write-Host ""
Write-Host "Or use the run.ps1 script: .\run.ps1" -ForegroundColor White
Write-Host ""
