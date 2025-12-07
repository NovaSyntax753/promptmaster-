# 🔑 Credentials Setup Guide

Follow these steps to configure your application with the credentials you collected.

---

## 📋 What You Need

Before starting, make sure you have:

- [ ] Supabase Project URL
- [ ] Supabase Anon Key (public key)
- [ ] Supabase Service Role Key (secret key)
- [ ] Supabase JWT Secret
- [ ] Database Password (from when you created the project)
- [ ] OpenRouter API Key

---

## 🔧 Step 1: Create Backend .env File

1. **Open PowerShell in your project folder:**

```powershell
cd "d:\Project\prompt analyst\backend"
```

2. **Copy the example file:**

```powershell
Copy-Item .env.example .env
```

3. **Edit the .env file:**

```powershell
notepad .env
```

4. **Replace the placeholders with your actual values:**

```bash
# Supabase Configuration
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=eyJhbGc...your-service-role-key...
SUPABASE_JWT_SECRET=your-jwt-secret-here

# Database
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@db.xxxxx.supabase.co:5432/postgres

# AI API
OPENROUTER_API_KEY=sk-or-v1-...your-openrouter-key...

# Application Settings (leave these as-is)
ENVIRONMENT=development
API_V1_STR=/api
PROJECT_NAME=PromptMaster
BACKEND_CORS_ORIGINS=["http://localhost:5173", "http://localhost:3000"]
```

**Important Notes:**

- `SUPABASE_KEY` = Use the **service_role** key (NOT the anon key)
- Replace `YOUR_PASSWORD` in DATABASE_URL with your database password
- Replace `xxxxx` with your actual project ID

5. **Save and close** (Ctrl+S, then close Notepad)

---

## 🎨 Step 2: Create Frontend .env File

1. **Go to frontend folder:**

```powershell
cd "d:\Project\prompt analyst\frontend"
```

2. **Copy the example file:**

```powershell
Copy-Item .env.example .env
```

3. **Edit the .env file:**

```powershell
notepad .env
```

4. **Replace with your values:**

```bash
VITE_SUPABASE_URL=https://xxxxx.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGc...your-anon-public-key...
VITE_API_URL=http://localhost:8000
```

**Important Notes:**

- `VITE_SUPABASE_ANON_KEY` = Use the **anon public** key (NOT the service_role key)
- Keep `VITE_API_URL` as `http://localhost:8000` for development

5. **Save and close**

---

## ✅ Step 3: Verify Your Setup

### Check Backend .env:

```powershell
cd "d:\Project\prompt analyst\backend"
cat .env
```

You should see your actual values (not the placeholders).

### Check Frontend .env:

```powershell
cd "d:\Project\prompt analyst\frontend"
cat .env
```

You should see your actual values.

---

## 🚀 Step 4: Run the Application

### Option A: Use the Setup Script (Recommended)

```powershell
cd "d:\Project\prompt analyst"
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

This will:

- Install Python dependencies
- Install Node.js dependencies
- Set up the project

### Option B: Manual Setup

**Install Backend Dependencies:**

```powershell
cd "d:\Project\prompt analyst\backend"
python -m pip install -r requirements.txt
```

**Install Frontend Dependencies:**

```powershell
cd "d:\Project\prompt analyst\frontend"
npm install
```

---

## 🎯 Step 5: Start the Application

### Start Backend (Terminal 1):

```powershell
cd "d:\Project\prompt analyst"
.\start-backend.ps1
```

Or manually:

```powershell
cd "d:\Project\prompt analyst\backend"
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Start Frontend (Terminal 2 - Open a new terminal):

```powershell
cd "d:\Project\prompt analyst"
.\start-frontend.ps1
```

Or manually:

```powershell
cd "d:\Project\prompt analyst\frontend"
npm run dev
```

---

## 🌐 Step 6: Access the Application

Once both servers are running:

1. **Frontend:** http://localhost:5173
2. **Backend API:** http://localhost:8000
3. **API Docs:** http://localhost:8000/docs

---

## 🎉 Test Everything Works

1. Open http://localhost:5173
2. Click **"Sign Up"**
3. Create a test account
4. Browse the challenges
5. Try submitting a prompt
6. Check if you get evaluation scores and suggestions!

---

## ⚠️ Troubleshooting

### Backend won't start?

- Check if Python is installed: `python --version`
- Check if dependencies are installed: `pip list`
- Check .env file has correct values

### Frontend won't start?

- Check if Node.js is installed: `node --version`
- Check if dependencies are installed: `npm list`
- Try deleting `node_modules` and run `npm install` again

### API errors?

- Check if both backend and frontend are running
- Check browser console (F12) for errors
- Verify Supabase credentials are correct
- Test backend directly: http://localhost:8000/docs

### Database connection errors?

- Verify DATABASE_URL has correct password
- Check if Supabase project is active
- Verify JWT_SECRET is correct

---

## 🔒 Security Notes

- **NEVER commit .env files to Git** (they're in .gitignore)
- Keep your service_role key secret
- Only share anon key publicly (it's safe for frontend)
- Regenerate keys if accidentally exposed

---

## 📝 Quick Reference

### Where to Find Credentials in Supabase:

| Credential        | Location                                                      |
| ----------------- | ------------------------------------------------------------- |
| Project URL       | Settings → API → Project URL                                  |
| Anon Key          | Settings → API → anon public (under Project API keys)         |
| Service Role Key  | Settings → API → service_role (click "Reveal")                |
| JWT Secret        | Settings → API → JWT Settings → JWT Secret                    |
| Database Password | Settings → Database → Connection info (or reset if forgotten) |

### Database URL Format:

```
postgresql://postgres:PASSWORD@db.PROJECT_ID.supabase.co:5432/postgres
```

Replace:

- `PASSWORD` = Your database password
- `PROJECT_ID` = Your Supabase project ID (from URL)

---

**Ready to run? Let me know if you need help with any step!** 🚀
