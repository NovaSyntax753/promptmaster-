# 🚀 Quick Start Guide - PromptMaster

## What You Have Now

Your **PromptMaster** project is fully set up with:

✅ **Backend** (FastAPI + Python)
✅ **Frontend** (React + TailwindCSS)
✅ **Database Schema** (Supabase PostgreSQL)
✅ **Sample Challenges** (12 challenges across 4 categories)
✅ **AI Evaluation System** (OpenRouter integration)
✅ **Progress Tracking** (Charts and analytics)
✅ **Authentication** (Supabase Auth with Google OAuth)

## 📁 Project Structure

```
d:\Project\prompt analyst\
├── backend/                    # Python FastAPI backend
│   ├── app/
│   │   ├── api/               # API routes (auth, challenges, evaluate, progress)
│   │   ├── services/          # Business logic
│   │   ├── models/            # Data models
│   │   ├── core/              # Configuration
│   │   └── main.py            # FastAPI app
│   ├── requirements.txt       # Python dependencies
│   └── .env.example          # Environment template
│
├── frontend/                  # React frontend
│   ├── src/
│   │   ├── components/       # Layout component
│   │   ├── pages/            # All page components
│   │   ├── contexts/         # Auth context
│   │   ├── services/         # API & Supabase clients
│   │   └── App.jsx
│   ├── package.json          # Node dependencies
│   └── .env.example         # Environment template
│
├── database/                 # Database setup
│   ├── schema.sql           # Tables, indexes, RLS policies
│   └── seed.sql             # 12 sample challenges
│
├── setup.ps1                # Automated setup script
├── start-backend.ps1        # Start backend server
├── start-frontend.ps1       # Start frontend server
├── README.md                # Main documentation
├── SETUP.md                 # Detailed setup instructions
└── PROJECT_OVERVIEW.md      # Technical overview
```

## 🎯 Next Steps (In Order)

### 1️⃣ Run Setup Script

Open PowerShell in the project directory and run:

```powershell
.\setup.ps1
```

**⚠️ If you get an execution policy error**, use this instead:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\setup.ps1
```

Or see [EXECUTION_POLICY_FIX.md](EXECUTION_POLICY_FIX.md) for detailed solutions.

This will:

- Create Python virtual environment
- Install all backend dependencies
- Install all frontend dependencies
- Create `.env` files from templates

### 2️⃣ Set Up Supabase

1. Go to https://supabase.com and sign up
2. Create a new project (wait for initialization)
3. Go to SQL Editor and run:
   - `database/schema.sql` (creates tables)
   - `database/seed.sql` (adds 12 challenges)
4. Get your credentials from Project Settings:
   - Project URL
   - `anon` public key
   - `service_role` secret key
   - JWT Secret (from Auth settings)

### 3️⃣ Get OpenRouter API Key

1. Go to https://openrouter.ai and sign up
2. Get your API key from dashboard
3. Add credits (starts at $5)

### 4️⃣ Configure Environment Variables

**Backend** (`backend/.env`):

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-service-role-key
SUPABASE_JWT_SECRET=your-jwt-secret
DATABASE_URL=postgresql://postgres:password@db.your-project.supabase.co:5432/postgres
OPENROUTER_API_KEY=your-openrouter-key
```

**Frontend** (`frontend/.env`):

```env
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-public-key
VITE_API_URL=http://localhost:8000
```

### 5️⃣ Start the Application

**Option A: Use convenience scripts**

Open two PowerShell windows:

Window 1 (Backend):

```powershell
.\start-backend.ps1
```

Window 2 (Frontend):

```powershell
.\start-frontend.ps1
```

**Option B: Manual start**

Backend:

```powershell
cd backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000
```

Frontend (new window):

```powershell
cd frontend
npm run dev
```

### 6️⃣ Test the Application

1. Open browser to http://localhost:5173
2. Click "Sign Up" and create an account
3. Explore the dashboard
4. Try a challenge and submit a prompt!

## 🎨 Key Features to Try

### Dashboard

- View your total attempts
- See average score
- Check improvement rate
- View best category

### Challenges

- Filter by category (Creative Writing, Coding, etc.)
- Filter by difficulty (Beginner, Intermediate, Advanced)
- Read challenge goals and example prompts

### Submit a Prompt

1. Choose a challenge
2. Read the goal and example
3. Write your own prompt
4. Submit for AI evaluation
5. Get detailed scores and suggestions

### Progress Tracking

- View score trends over time
- See your top 3 common mistakes
- Analyze performance by category

## 🛠️ Troubleshooting

### Backend Won't Start

```powershell
# Reinstall dependencies
cd backend
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Frontend Won't Start

```powershell
# Clear and reinstall
cd frontend
Remove-Item -Recurse -Force node_modules
npm install
```

### Can't Connect to Supabase

- Verify your `.env` files have correct URLs and keys
- Check your Supabase project is fully initialized
- Ensure you ran both SQL scripts

### AI Evaluation Fails

- Verify OpenRouter API key is correct
- Check you have credits in OpenRouter account
- Review backend logs for error messages

## 📚 Documentation

- **SETUP.md** - Detailed setup instructions
- **README.md** - Project overview and features
- **PROJECT_OVERVIEW.md** - Technical architecture
- **API Docs** - Visit http://localhost:8000/docs when backend is running

## 🎓 Understanding the Code

### Backend Flow

1. User submits prompt → `evaluate.py` route
2. Route calls → `evaluation_service.py`
3. Service calls OpenRouter API twice:
   - Generate AI output from user prompt
   - Evaluate prompt quality
4. Store results in Supabase
5. Return to frontend

### Frontend Flow

1. User interaction → Page component
2. Component calls → `api.js` service
3. Service adds auth token → Makes HTTP request
4. Backend processes → Returns data
5. Component updates state → UI rerenders

## 💡 Customization Ideas

1. **Add More Challenges**

   - Edit `database/seed.sql`
   - Run new INSERT statements in Supabase

2. **Adjust Evaluation Criteria**

   - Edit `evaluation_service.py`
   - Modify the AI prompts for scoring

3. **Change AI Model**

   - Edit `backend/app/core/config.py`
   - Change `DEFAULT_MODEL` setting

4. **Customize UI**
   - Edit components in `frontend/src/`
   - Modify TailwindCSS classes
   - Change colors in `tailwind.config.js`

## 🚀 Deployment Options

### Backend

- **Railway** - Easy Python deployment
- **Render** - Free tier available
- **AWS/Azure** - Production scale

### Frontend

- **Vercel** - Optimized for React
- **Netlify** - Simple deployment
- **GitHub Pages** - Free static hosting

## 📞 Support

If you encounter issues:

1. Check the error messages in terminal/console
2. Review the SETUP.md for detailed steps
3. Verify all environment variables are set
4. Check Supabase dashboard for database issues
5. Review backend logs at http://localhost:8000/docs

## 🎉 You're Ready!

Your PromptMaster application is fully configured and ready to use. Start by running the setup script and following the steps above.

**Happy prompting! 🚀**

---

**Quick Command Reference:**

```powershell
# Setup (one time)
.\setup.ps1

# Start backend
.\start-backend.ps1

# Start frontend
.\start-frontend.ps1

# View API docs
# Open: http://localhost:8000/docs

# Access app
# Open: http://localhost:5173
```
