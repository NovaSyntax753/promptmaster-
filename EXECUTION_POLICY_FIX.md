# PromptMaster Setup - PowerShell Execution Policy Issue

## ❌ Error You're Seeing

```
.\setup.ps1 : File D:\Project\prompt analyst\setup.ps1 cannot be loaded because running scripts is
disabled on this system.
```

This happens because Windows PowerShell has execution policies that prevent running scripts for security.

## ✅ Solutions (Choose One)

### **Solution 1: Bypass Execution Policy (Recommended)**

Run the script with a bypass flag (one-time, safe for this script):

```powershell
PowerShell -ExecutionPolicy Bypass -File ".\setup.ps1"
```

Or if you're already in the project directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

---

### **Solution 2: Change Execution Policy for Current User**

This allows you to run scripts in the future:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then run:

```powershell
.\setup.ps1
```

**Note:** You may need to restart PowerShell after changing the policy.

---

### **Solution 3: Run Commands Manually (If Scripts Still Don't Work)**

If you prefer not to change execution policies, follow these manual steps:

#### **Step 1: Backend Setup**

```powershell
# Navigate to backend directory
cd "d:\Project\prompt analyst\backend"

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If activation also fails due to execution policy, use:
# PowerShell -ExecutionPolicy Bypass -File .\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env file
Copy-Item .env.example .env

# Deactivate for now
deactivate

# Go back to project root
cd ..
```

#### **Step 2: Frontend Setup**

```powershell
# Navigate to frontend directory
cd "d:\Project\prompt analyst\frontend"

# Install dependencies
npm install

# Create .env file
Copy-Item .env.example .env

# Go back to project root
cd ..
```

---

### **Solution 4: Use Windows Command Prompt Instead**

If PowerShell is too restrictive, use Command Prompt (cmd.exe):

#### **Backend Setup (cmd):**

```cmd
cd "d:\Project\prompt analyst\backend"
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
copy .env.example .env
deactivate
cd ..
```

#### **Frontend Setup (cmd):**

```cmd
cd "d:\Project\prompt analyst\frontend"
npm install
copy .env.example .env
cd ..
```

---

## 🚀 After Setup - Starting the Application

### If You Fixed PowerShell Execution Policy:

**Backend:**

```powershell
.\start-backend.ps1
```

**Frontend:**

```powershell
.\start-frontend.ps1
```

### If Scripts Still Don't Work:

**Backend (PowerShell):**

```powershell
cd "d:\Project\prompt analyst\backend"
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000
```

Or with bypass:

```powershell
cd "d:\Project\prompt analyst\backend"
PowerShell -ExecutionPolicy Bypass -File .\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000
```

**Frontend (PowerShell - new window):**

```powershell
cd "d:\Project\prompt analyst\frontend"
npm run dev
```

**Backend (Command Prompt):**

```cmd
cd "d:\Project\prompt analyst\backend"
venv\Scripts\activate.bat
uvicorn app.main:app --reload --port 8000
```

**Frontend (Command Prompt - new window):**

```cmd
cd "d:\Project\prompt analyst\frontend"
npm run dev
```

---

## 🔍 Understanding Execution Policies

PowerShell has several execution policy levels:

- **Restricted** - No scripts allowed (default on Windows clients)
- **RemoteSigned** - Local scripts allowed, downloaded scripts must be signed
- **Unrestricted** - All scripts allowed (with warning for downloaded scripts)
- **Bypass** - Nothing is blocked, no warnings

### Check Your Current Policy:

```powershell
Get-ExecutionPolicy
```

### See All Policy Scopes:

```powershell
Get-ExecutionPolicy -List
```

---

## 📋 Quick Setup Commands (Copy & Paste)

### Option A: Use Bypass (Safest)

```powershell
cd "d:\Project\prompt analyst"
PowerShell -ExecutionPolicy Bypass -File .\setup.ps1
```

### Option B: Change Policy Then Run

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
cd "d:\Project\prompt analyst"
.\setup.ps1
```

### Option C: Manual Setup

```powershell
# Backend
cd "d:\Project\prompt analyst\backend"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
deactivate

# Frontend
cd "d:\Project\prompt analyst\frontend"
npm install
Copy-Item .env.example .env
```

---

## ✅ Next Steps After Setup

1. **Configure Supabase** (see QUICKSTART.md step 2)
2. **Get OpenRouter API Key** (see QUICKSTART.md step 3)
3. **Edit .env files** with your credentials:
   - `backend\.env`
   - `frontend\.env`
4. **Start the application**

---

## 💡 Recommended Approach

**For this one-time setup, I recommend:**

```powershell
cd "d:\Project\prompt analyst"
PowerShell -ExecutionPolicy Bypass -File .\setup.ps1
```

This is safe and doesn't require permanently changing your system settings.

**For starting the servers later, you can:**

Either use the same bypass method:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\start-backend.ps1
PowerShell -ExecutionPolicy Bypass -File .\start-frontend.ps1
```

Or run the commands manually (they're simple):

```powershell
# Backend
cd backend; .\venv\Scripts\Activate.ps1; uvicorn app.main:app --reload

# Frontend (new window)
cd frontend; npm run dev
```

---

## 🆘 Still Having Issues?

If the Activate.ps1 script also fails:

**Use Command Prompt (cmd.exe) instead:**

- Open Command Prompt (not PowerShell)
- Run: `cmd` in your current PowerShell window
- Then follow the Command Prompt instructions above

**Or activate with bypass:**

```powershell
cd backend
PowerShell -ExecutionPolicy Bypass -File .\venv\Scripts\Activate.ps1
```

---

**Let me know if you need any clarification! 🚀**
