# PromptMaster Quick Start Script
# Run this script to set up the project quickly

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   PromptMaster Setup Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version
    Write-Host "✓ $pythonVersion found" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install Python 3.9 or higher." -ForegroundColor Red
    exit 1
}

# Check Node.js
Write-Host "Checking Node.js installation..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version
    Write-Host "✓ Node.js $nodeVersion found" -ForegroundColor Green
} catch {
    Write-Host "✗ Node.js not found. Please install Node.js 18 or higher." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Setting up Backend" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Backend setup
Set-Location backend

# Create virtual environment
Write-Host "Creating Python virtual environment..." -ForegroundColor Yellow
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Create .env if it doesn't exist
if (!(Test-Path .env)) {
    Write-Host "Creating .env file from template..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host "✓ .env file created. Please edit it with your credentials." -ForegroundColor Green
} else {
    Write-Host "✓ .env file already exists" -ForegroundColor Green
}

# Deactivate venv for now
deactivate

Set-Location ..

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Setting up Frontend" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Frontend setup
Set-Location frontend

# Install dependencies
Write-Host "Installing Node.js dependencies..." -ForegroundColor Yellow
npm install

# Create .env if it doesn't exist
if (!(Test-Path .env)) {
    Write-Host "Creating .env file from template..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host "✓ .env file created. Please edit it with your credentials." -ForegroundColor Green
} else {
    Write-Host "✓ .env file already exists" -ForegroundColor Green
}

Set-Location ..

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Set up your Supabase project and run the SQL scripts" -ForegroundColor White
Write-Host "2. Edit backend/.env with your Supabase and OpenRouter credentials" -ForegroundColor White
Write-Host "3. Edit frontend/.env with your Supabase credentials" -ForegroundColor White
Write-Host ""
Write-Host "To start the application:" -ForegroundColor Yellow
Write-Host "  Backend:  cd backend; .\venv\Scripts\Activate.ps1; uvicorn app.main:app --reload" -ForegroundColor White
Write-Host "  Frontend: cd frontend; npm run dev" -ForegroundColor White
Write-Host ""
Write-Host "For detailed instructions, see SETUP.md" -ForegroundColor Cyan
Write-Host ""
