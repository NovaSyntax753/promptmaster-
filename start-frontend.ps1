# PromptMaster - Start Frontend Server

Write-Host "Starting PromptMaster Frontend..." -ForegroundColor Cyan

Set-Location frontend

Write-Host "Frontend running at http://localhost:5173" -ForegroundColor Green
Write-Host ""

npm run dev
