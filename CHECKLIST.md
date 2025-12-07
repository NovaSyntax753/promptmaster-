# PromptMaster Setup Checklist

Use this checklist to ensure you've completed all setup steps correctly.

## ✅ Prerequisites

- [ ] Python 3.9+ installed (`python --version`)
- [ ] Node.js 18+ installed (`node --version`)
- [ ] Git installed (optional, for version control)
- [ ] Code editor (VS Code recommended)
- [ ] Modern web browser (Chrome, Firefox, Edge)

## ✅ Project Setup

- [ ] Navigated to project directory: `d:\Project\prompt analyst`
- [ ] Reviewed README.md to understand the project
- [ ] Reviewed QUICKSTART.md for quick overview

## ✅ Automated Setup

- [ ] Ran `.\setup.ps1` successfully
- [ ] Backend virtual environment created (backend/venv/)
- [ ] Backend dependencies installed
- [ ] Frontend dependencies installed (frontend/node_modules/)
- [ ] `.env` files created in both backend and frontend

## ✅ Supabase Configuration

### Create Project

- [ ] Created account at https://supabase.com
- [ ] Created new project
- [ ] Waited for project initialization to complete
- [ ] Noted project name and region

### Run Database Scripts

- [ ] Opened Supabase SQL Editor
- [ ] Ran `database/schema.sql` successfully
  - [ ] Tables created (challenges, evaluations)
  - [ ] Indexes created
  - [ ] RLS policies enabled
  - [ ] Functions and views created
- [ ] Ran `database/seed.sql` successfully
  - [ ] 12 challenges inserted
  - [ ] Verified data in Table Editor

### Get Credentials

- [ ] Copied Project URL from Project Settings > API
- [ ] Copied `anon` public key from Project Settings > API
- [ ] Copied `service_role` secret key from Project Settings > API
- [ ] Copied JWT Secret from Project Settings > Auth > JWT Settings
- [ ] Copied Database connection string (PostgreSQL)

### Optional: Enable Google OAuth

- [ ] Went to Authentication > Providers
- [ ] Enabled Google provider
- [ ] Configured OAuth credentials (if using Google sign-in)

## ✅ OpenRouter Configuration

- [ ] Created account at https://openrouter.ai
- [ ] Generated API key from dashboard
- [ ] Added credits to account ($5 minimum)
- [ ] Tested API key is active
- [ ] Noted preferred AI model (default: Mistral 7B)

## ✅ Backend Configuration

### Environment Variables (backend/.env)

- [ ] Opened `backend/.env` in editor
- [ ] Set `SUPABASE_URL=` (from Supabase)
- [ ] Set `SUPABASE_KEY=` (service role key)
- [ ] Set `SUPABASE_JWT_SECRET=` (from Supabase)
- [ ] Set `DATABASE_URL=` (PostgreSQL connection string)
- [ ] Set `OPENROUTER_API_KEY=` (from OpenRouter)
- [ ] Saved file

### Verify Backend

- [ ] Activated virtual environment: `backend\venv\Scripts\Activate.ps1`
- [ ] All Python packages installed: `pip list`
- [ ] No import errors when running: `python -c "from app.main import app"`

## ✅ Frontend Configuration

### Environment Variables (frontend/.env)

- [ ] Opened `frontend/.env` in editor
- [ ] Set `VITE_SUPABASE_URL=` (from Supabase)
- [ ] Set `VITE_SUPABASE_ANON_KEY=` (anon public key)
- [ ] Set `VITE_API_URL=http://localhost:8000`
- [ ] Saved file

### Verify Frontend

- [ ] All Node packages installed: `npm list --depth=0`
- [ ] No dependency errors

## ✅ Start Application

### Backend Server

- [ ] Opened PowerShell window #1
- [ ] Navigated to project root
- [ ] Ran `.\start-backend.ps1` OR manual start:
  ```powershell
  cd backend
  .\venv\Scripts\Activate.ps1
  uvicorn app.main:app --reload --port 8000
  ```
- [ ] Server started successfully
- [ ] No error messages in console
- [ ] Visited http://localhost:8000 - saw welcome message
- [ ] Visited http://localhost:8000/docs - saw API documentation
- [ ] Tried http://localhost:8000/health - got `{"status":"healthy"}`

### Frontend Server

- [ ] Opened PowerShell window #2
- [ ] Navigated to project root
- [ ] Ran `.\start-frontend.ps1` OR manual start:
  ```powershell
  cd frontend
  npm run dev
  ```
- [ ] Server started successfully
- [ ] Saw "Local: http://localhost:5173" in console
- [ ] No compilation errors

## ✅ Test Application

### Initial Access

- [ ] Opened browser to http://localhost:5173
- [ ] Saw PromptMaster login page
- [ ] Page loaded without errors
- [ ] No errors in browser console (F12)

### User Registration

- [ ] Clicked "Sign Up" link
- [ ] Filled in registration form:
  - [ ] Full Name
  - [ ] Email address
  - [ ] Password (6+ characters)
  - [ ] Confirm Password (matching)
- [ ] Clicked "Create account"
- [ ] Account created successfully
- [ ] Redirected to dashboard
- [ ] No error messages

### Dashboard

- [ ] Dashboard page loaded
- [ ] Saw navigation: Dashboard, Challenges, History, Progress
- [ ] Saw statistics cards (all zeros for new user)
- [ ] Saw user email in top right
- [ ] "Sign Out" button visible
- [ ] Quick actions cards displayed

### Browse Challenges

- [ ] Clicked "Challenges" in navigation
- [ ] Saw list of 12 challenges
- [ ] Category filter works (Creative Writing, Coding, etc.)
- [ ] Difficulty filter works (Beginner, Intermediate, Advanced)
- [ ] Challenge cards display properly
- [ ] Hovering shows interactive effects

### Complete a Challenge

- [ ] Clicked on a beginner challenge
- [ ] Challenge detail page loaded
- [ ] Saw challenge goal clearly
- [ ] Saw example prompt
- [ ] Category and difficulty badges visible
- [ ] Text area for prompt input ready
- [ ] Wrote a test prompt (at least 50 words)
- [ ] Clicked "Submit for Evaluation"
- [ ] Saw loading indicator
- [ ] Evaluation completed (15-30 seconds)
- [ ] Received results:
  - [ ] Overall score displayed (0-10)
  - [ ] Score breakdown for all 4 criteria
  - [ ] Visual progress bars
  - [ ] Improvement suggestions listed
  - [ ] AI generated output shown
- [ ] "Try Again" button works
- [ ] "Next Challenge" link works

### View History

- [ ] Clicked "History" in navigation
- [ ] Saw previous evaluation listed
- [ ] Evaluation shows:
  - [ ] Challenge number
  - [ ] Date and time
  - [ ] Overall score
  - [ ] Prompt preview
  - [ ] Individual scores
  - [ ] Number of suggestions
- [ ] "Retry" button links to challenge

### View Progress

- [ ] Clicked "Progress" in navigation
- [ ] Time range selector works (7/30/90 days)
- [ ] Score trend chart displays (if data available)
- [ ] Top mistakes section shows (if data available)
- [ ] Insights section displays helpful tips

### Sign Out and Sign In

- [ ] Clicked "Sign Out" button
- [ ] Redirected to login page
- [ ] Entered email and password
- [ ] Clicked "Sign in"
- [ ] Successfully logged in
- [ ] Returned to dashboard with data intact

## ✅ Troubleshooting Verification

If you encountered issues, verify these were resolved:

### Backend Issues

- [ ] Virtual environment activated before starting server
- [ ] All environment variables set correctly
- [ ] No port conflicts (8000 available)
- [ ] Firewall not blocking local connections
- [ ] Python version compatible (3.9+)

### Frontend Issues

- [ ] Node modules installed completely
- [ ] No conflicting processes on port 5173
- [ ] Environment variables use VITE\_ prefix
- [ ] CORS enabled in backend (should be by default)
- [ ] Browser allows localhost connections

### Database Issues

- [ ] Supabase project fully initialized
- [ ] SQL scripts ran without errors
- [ ] RLS policies not blocking operations
- [ ] Database URL connection string correct
- [ ] Service role key has proper permissions

### API Issues

- [ ] OpenRouter API key valid and active
- [ ] OpenRouter account has credits
- [ ] Network connection stable
- [ ] API requests not blocked by firewall
- [ ] Response timeout sufficient (30s)

## ✅ Optional Enhancements

- [ ] Enabled Google OAuth in Supabase
- [ ] Tested Google sign-in flow
- [ ] Added more custom challenges via Supabase
- [ ] Customized UI colors in tailwind.config.js
- [ ] Changed AI model in backend config
- [ ] Adjusted evaluation prompts
- [ ] Set up git repository
- [ ] Created first git commit

## ✅ Documentation Review

- [ ] Read README.md completely
- [ ] Reviewed SETUP.md for details
- [ ] Checked QUICKSTART.md for overview
- [ ] Reviewed PROJECT_OVERVIEW.md for architecture
- [ ] Examined ARCHITECTURE.md for data flow
- [ ] Bookmarked API docs (http://localhost:8000/docs)

## ✅ Development Environment

- [ ] Backend logs visible and readable
- [ ] Frontend hot reload working
- [ ] Browser DevTools familiar (F12)
- [ ] API docs accessible for testing
- [ ] Supabase dashboard accessible
- [ ] OpenRouter dashboard accessible

## ✅ Ready for Development!

If all items above are checked, you're ready to:

- ✨ Customize the application
- 🎨 Modify the UI/UX
- 🚀 Add new features
- 📝 Create more challenges
- 🔧 Experiment with AI models
- 📊 Enhance analytics

---

## 📋 Quick Reference

**Start Backend:**

```powershell
.\start-backend.ps1
```

**Start Frontend:**

```powershell
.\start-frontend.ps1
```

**Backend URL:** http://localhost:8000
**Frontend URL:** http://localhost:5173
**API Docs:** http://localhost:8000/docs

**Supabase Dashboard:** https://app.supabase.com
**OpenRouter Dashboard:** https://openrouter.ai/dashboard

---

## 🆘 Need Help?

If you're stuck on any step:

1. ❌ **Unchecked items** - Go back and complete those steps
2. 📖 **Detailed Steps** - Check SETUP.md for more information
3. 🔍 **Error Messages** - Read terminal/console output carefully
4. 🐛 **Debug** - Check browser console (F12) and backend logs
5. 🔑 **Environment** - Verify all .env variables are correct
6. 🔄 **Restart** - Try stopping and restarting both servers

**Happy Coding! 🚀**
