# PromptMaster - Start Backend Server

Write-Host "Starting PromptMaster Backend..." -ForegroundColor Cyan

Set-Location backend

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Start server
Write-Host "Backend running at http://localhost:8000" -ForegroundColor Green
Write-Host "API docs available at http://localhost:8000/docs" -ForegroundColor Green
Write-Host ""

uvicorn app.main:app --reload --port 8000
