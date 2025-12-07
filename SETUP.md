# PromptMaster Setup Guide

This guide will help you set up and run the PromptMaster application locally.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or higher
- Node.js 18 or higher
- Git

## Step 1: Clone or Navigate to Project

```powershell
cd "d:\Project\prompt analyst"
```

## Step 2: Set Up Supabase

1. Go to [https://supabase.com](https://supabase.com) and create a free account
2. Create a new project
3. Wait for the project to be fully initialized

### Configure Database

1. Go to the SQL Editor in your Supabase dashboard
2. Copy the contents of `database/schema.sql` and run it
3. Copy the contents of `database/seed.sql` and run it

### Get API Keys

1. Go to Project Settings > API
2. Copy your Project URL
3. Copy your `anon` public key
4. Copy your `service_role` secret key (keep this secure!)
5. Go to Project Settings > Auth > JWT Secret and copy it

### Enable Google OAuth (Optional)

1. Go to Authentication > Providers
2. Enable Google provider
3. Add your Google OAuth credentials

## Step 3: Set Up Backend

```powershell
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
Copy-Item .env.example .env

# Edit .env file with your credentials
notepad .env
```

Fill in your `.env` file with:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_service_role_key
SUPABASE_JWT_SECRET=your_jwt_secret
DATABASE_URL=your_postgres_connection_string
OPENROUTER_API_KEY=your_openrouter_api_key
```

### Get OpenRouter API Key

1. Go to [https://openrouter.ai](https://openrouter.ai)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Add credits (starts at $5)

### Run Backend

```powershell
# Make sure you're in the backend directory with venv activated
uvicorn app.main:app --reload --port 8000
```

The backend should now be running at `http://localhost:8000`
Visit `http://localhost:8000/docs` to see the API documentation.

## Step 4: Set Up Frontend

Open a new PowerShell window:

```powershell
cd "d:\Project\prompt analyst\frontend"

# Install dependencies
npm install

# Create .env file
Copy-Item .env.example .env

# Edit .env file
notepad .env
```

Fill in your `.env` file with:

```env
VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_ANON_KEY=your_anon_public_key
VITE_API_URL=http://localhost:8000
```

### Run Frontend

```powershell
npm run dev
```

The frontend should now be running at `http://localhost:5173`

## Step 5: Test the Application

1. Open your browser and go to `http://localhost:5173`
2. Click "Sign Up" and create a new account
3. After signing in, you should see the dashboard
4. Browse challenges and try submitting a prompt!

## Troubleshooting

### Backend Issues

**Error: Module not found**

```powershell
pip install -r requirements.txt
```

**Error: Cannot connect to Supabase**

- Check your `SUPABASE_URL` and `SUPABASE_KEY` in `.env`
- Ensure your Supabase project is fully initialized

**Error: OpenRouter API key invalid**

- Verify your API key at [https://openrouter.ai](https://openrouter.ai)
- Ensure you have credits in your account

### Frontend Issues

**Error: Cannot connect to backend**

- Ensure backend is running on port 8000
- Check `VITE_API_URL` in frontend `.env`

**Error: Supabase auth not working**

- Verify `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY`
- Check Supabase project status

**Error: Module not found**

```powershell
rm -r node_modules
npm install
```

## Development Tips

### Backend Development

- API docs available at `http://localhost:8000/docs`
- Logs are shown in the terminal where you ran `uvicorn`
- Hot reload is enabled - changes are reflected automatically

### Frontend Development

- Vite provides hot module replacement
- React DevTools browser extension is helpful
- Check browser console for errors

## Project Structure

```
prompt-analyst/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API routes
│   │   ├── core/        # Configuration
│   │   ├── models/      # Data models
│   │   ├── services/    # Business logic
│   │   └── main.py      # Entry point
│   └── requirements.txt
├── frontend/            # React frontend
│   ├── src/
│   │   ├── components/  # Reusable components
│   │   ├── pages/       # Page components
│   │   ├── services/    # API services
│   │   └── contexts/    # React contexts
│   └── package.json
├── database/            # Database setup
│   ├── schema.sql      # Database schema
│   └── seed.sql        # Sample data
└── README.md
```

## Next Steps

- Add more challenges in Supabase
- Customize the AI evaluation prompts
- Deploy to production (see README.md)
- Explore the code and make it your own!

## Getting Help

- Check the API documentation at `/docs`
- Review error logs in terminal
- Check browser console for frontend errors
- Verify all environment variables are set correctly

Enjoy building with PromptMaster! 🚀
