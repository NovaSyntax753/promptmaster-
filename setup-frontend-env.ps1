# Frontend Environment Setup Helper
# This script helps you create the frontend .env file

Write-Host "=== Frontend Environment Setup ===" -ForegroundColor Cyan
Write-Host ""

$envPath = "frontend\.env"

if (Test-Path $envPath) {
    Write-Host "⚠️  .env file already exists at: $envPath" -ForegroundColor Yellow
    $overwrite = Read-Host "Do you want to overwrite it? (y/n)"
    if ($overwrite -ne "y") {
        Write-Host "Cancelled." -ForegroundColor Red
        exit
    }
}

Write-Host "Please provide your Supabase credentials:" -ForegroundColor Green
Write-Host "You can find these at: https://supabase.com/dashboard" -ForegroundColor Gray
Write-Host "  Go to: Project Settings > API" -ForegroundColor Gray
Write-Host ""

$supabaseUrl = Read-Host "Enter your Supabase URL (e.g., https://xxxxx.supabase.co)"
$supabaseAnonKey = Read-Host "Enter your Supabase Anon Key (the public/anon key, NOT service_role)"

# Validate inputs
if ([string]::IsNullOrWhiteSpace($supabaseUrl) -or [string]::IsNullOrWhiteSpace($supabaseAnonKey)) {
    Write-Host "❌ Error: Both values are required!" -ForegroundColor Red
    exit 1
}

# Create .env content
$envContent = @"
# Supabase Configuration
VITE_SUPABASE_URL=$supabaseUrl
VITE_SUPABASE_ANON_KEY=$supabaseAnonKey
VITE_API_URL=http://localhost:8000
"@

# Write to file
try {
    Set-Content -Path $envPath -Value $envContent -ErrorAction Stop
    Write-Host ""
    Write-Host "✅ .env file created successfully at: $envPath" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Cyan
    Write-Host "1. Restart your frontend dev server (stop it with Ctrl+C, then run 'npm run dev' again)" -ForegroundColor White
    Write-Host "2. Try logging in again" -ForegroundColor White
    Write-Host ""
} catch {
    Write-Host "❌ Error creating .env file: $_" -ForegroundColor Red
    exit 1
}



