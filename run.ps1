# Google Maps Scraper - Run Script
# Quick script to run the application

# Activate virtual environment
if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & .\venv\Scripts\Activate.ps1
} else {
    Write-Host "Virtual environment not found. Please run setup.ps1 first." -ForegroundColor Red
    exit 1
}

# Run the application
Write-Host "Starting Google Maps Scraper..." -ForegroundColor Green
Write-Host ""
python main.py
