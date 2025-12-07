# Complete Supabase Setup Guide for PromptMaster

This guide will walk you through setting up Supabase from scratch, step by step.

## 📋 Table of Contents

1. [Create Supabase Account](#step-1-create-supabase-account)
2. [Create New Project](#step-2-create-new-project)
3. [Run Database Schema](#step-3-run-database-schema)
4. [Run Seed Data](#step-4-run-seed-data)
5. [Get API Credentials](#step-5-get-api-credentials)
6. [Configure Your Application](#step-6-configure-your-application)
7. [Verify Setup](#step-7-verify-setup)

---

## Step 1: Create Supabase Account

### 1.1 Go to Supabase Website

- Open your browser
- Visit: **https://supabase.com**
- Click the **"Start your project"** or **"Sign up"** button

### 1.2 Sign Up

You have three options:

- **GitHub**: Click "Continue with GitHub" (recommended, fastest)
- **Email**: Enter your email and create a password
- **Google**: Click "Continue with Google"

### 1.3 Verify Email

- Check your email inbox
- Click the verification link
- You'll be redirected to Supabase dashboard

---

## Step 2: Create New Project

### 2.1 Access Dashboard

- After logging in, you'll see the Supabase dashboard
- Click the **"New Project"** button (green button, top right)

### 2.2 Select Organization

- If this is your first time:
  - Click **"Create a new organization"**
  - Enter organization name (e.g., "My Projects" or your name)
  - Click **"Create organization"**
- If you already have an organization:
  - Select it from the dropdown

### 2.3 Fill in Project Details

**Project Name:**

```
PromptMaster
```

(or any name you prefer)

**Database Password:**

- **IMPORTANT**: Save this password somewhere safe!
- You'll need it later for the DATABASE_URL
- Use a strong password (Supabase will generate one, or create your own)
- Example: `MySecurePass123!@#`

**Region:**

- Choose the region closest to you
- Examples:
  - US: `US East (North Virginia)` or `US West (Oregon)`
  - Europe: `Europe (Frankfurt)` or `Europe (London)`
  - Asia: `Asia (Singapore)` or `Asia (Tokyo)`

**Pricing Plan:**

- Select **"Free"** (perfect for this project)
- Includes: 500MB database, 1GB file storage, 50MB file uploads

### 2.4 Create Project

- Click **"Create new project"**
- Wait 2-3 minutes for initialization
- You'll see a progress indicator
- **DO NOT CLOSE THE TAB** during setup

### 2.5 Project Ready

- When complete, you'll see: "Project is ready"
- You'll be on the project dashboard

---

## Step 3: Run Database Schema

This creates the tables, indexes, and security policies.

### 3.1 Open SQL Editor

- In the left sidebar, find and click **"SQL Editor"**
- Or click **"Database"** → **"SQL Editor"**

### 3.2 Open Schema File

- On your computer, navigate to:
  ```
  d:\Project\prompt analyst\database\schema.sql
  ```
- Open this file with Notepad or your code editor
- **Select all** (Ctrl+A) and **Copy** (Ctrl+C)

### 3.3 Paste and Run

- Back in Supabase SQL Editor
- Click **"+ New query"** button
- You'll see an empty SQL editor
- **Paste** (Ctrl+V) the entire schema.sql contents
- Click the **"Run"** button (or press Ctrl+Enter)

### 3.4 Verify Success

You should see:

```
Success. No rows returned
```

If you see any errors:

- Read the error message carefully
- Make sure you copied the entire file
- Check that the project finished initializing
- Try running it again

### 3.5 Check Tables Created

- Click **"Table Editor"** in the left sidebar
- You should see two tables:
  1. **challenges**
  2. **evaluations**
- Click on each to verify they exist

---

## Step 4: Run Seed Data

This adds 12 sample challenges to your database.

### 4.1 Open New Query

- Still in SQL Editor
- Click **"+ New query"** button again

### 4.2 Open Seed File

- On your computer, navigate to:
  ```
  d:\Project\prompt analyst\database\seed.sql
  ```
- Open this file with Notepad or your code editor
- **Select all** (Ctrl+A) and **Copy** (Ctrl+C)

### 4.3 Paste and Run

- Back in Supabase SQL Editor
- **Paste** (Ctrl+V) the entire seed.sql contents
- Click the **"Run"** button (or press Ctrl+Enter)

### 4.4 Verify Success

You should see:

```
Success. No rows returned
```

### 4.5 Check Data Inserted

- Click **"Table Editor"** in the left sidebar
- Click on the **"challenges"** table
- You should see 12 rows of data:
  - 3 Creative Writing challenges
  - 3 Coding & Debugging challenges
  - 3 Summarization & Rewriting challenges
  - 3 Data Extraction challenges
- Each with different difficulty levels (beginner, intermediate, advanced)

---

## Step 5: Get API Credentials

Now you need to get 4 important pieces of information.

### 5.1 Get Project URL and API Keys

#### Open Project Settings:

- Click the **"Settings"** icon (gear icon) in the left sidebar
- Or click your project name → **"Settings"**

#### Navigate to API Section:

- In Settings menu, click **"API"**
- You'll see the API settings page

#### Copy These Values:

**1. Project URL:**

- Look for **"Project URL"** or **"URL"**
- It looks like: `https://abcdefghijklmnop.supabase.co`
- Click the **copy icon** next to it
- Save it in a text file

**2. anon public Key:**

- Scroll down to **"Project API keys"** section
- Find **"anon" "public"** key
- It's a long string starting with `eyJ...`
- Click the **copy icon**
- Save it in your text file
- **Label it**: "anon key"

**3. service_role secret Key:**

- In the same **"Project API keys"** section
- Find **"service_role" "secret"** key
- Click **"Reveal"** button first (it's hidden by default)
- It's another long string starting with `eyJ...`
- Click the **copy icon**
- Save it in your text file
- **Label it**: "service_role key"
- ⚠️ **KEEP THIS SECRET!** Never share or commit to GitHub

### 5.2 Get JWT Secret

#### Navigate to Auth Settings:

- Still in Settings menu
- Click **"Auth"** in the left sidebar

#### Find JWT Settings:

- Scroll down to find **"JWT Settings"** section
- Or look for **"JWT Secret"**

#### Copy JWT Secret:

- Click **"Reveal"** to show the secret
- Copy the JWT secret
- Save it in your text file
- **Label it**: "JWT Secret"

### 5.3 Get Database Connection String

#### Navigate to Database Settings:

- In Settings menu, click **"Database"**

#### Find Connection String:

- Scroll down to **"Connection string"** section
- Select **"URI"** tab
- You'll see a connection string like:
  ```
  postgresql://postgres:[YOUR-PASSWORD]@db.abcdefghijklmnop.supabase.co:5432/postgres
  ```

#### Update with Your Password:

- Replace `[YOUR-PASSWORD]` with the database password you created in Step 2.2
- Example:
  ```
  postgresql://postgres:MySecurePass123!@#@db.abcdefghijklmnop.supabase.co:5432/postgres
  ```
- Copy the complete string
- Save it in your text file
- **Label it**: "Database URL"

### 5.4 Summary - You Should Now Have:

```
1. Project URL: https://abcdefghijklmnop.supabase.co
2. anon key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
3. service_role key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
4. JWT Secret: your-jwt-secret-string-here
5. Database URL: postgresql://postgres:password@db.xxx.supabase.co:5432/postgres
```

---

## Step 6: Configure Your Application

Now use these credentials in your project.

### 6.1 Configure Backend

#### Open Backend .env File:

```powershell
notepad "d:\Project\prompt analyst\backend\.env"
```

#### Fill in the Values:

```env
# Replace these with YOUR actual values from Supabase

SUPABASE_URL=https://abcdefghijklmnop.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFiY2RlZmdoaWprbG1ub3AiLCJyb2xlIjoic2VydmljZV9yb2xlIiwiaWF0IjoxNjg5MDAwMDAwLCJleHAiOjE4NDY3ODAwMDB9.xxxxxxxxxxxxx
SUPABASE_JWT_SECRET=your-jwt-secret-here
DATABASE_URL=postgresql://postgres:YourPassword123@db.abcdefghijklmnop.supabase.co:5432/postgres
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# Keep these as is
ENVIRONMENT=development
API_V1_STR=/api
PROJECT_NAME=PromptMaster
BACKEND_CORS_ORIGINS=["http://localhost:5173", "http://localhost:3000"]
```

**Important Notes:**

- Use the **service_role** key for SUPABASE_KEY (not the anon key)
- Make sure there are no spaces around the `=` signs
- Don't use quotes around the values (except for BACKEND_CORS_ORIGINS)

#### Save and Close

### 6.2 Configure Frontend

#### Open Frontend .env File:

```powershell
notepad "d:\Project\prompt analyst\frontend\.env"
```

#### Fill in the Values:

```env
# Replace these with YOUR actual values from Supabase

VITE_SUPABASE_URL=https://abcdefghijklmnop.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFiY2RlZmdoaWprbG1ub3AiLCJyb2xlIjoiYW5vbiIsImlhdCI6MTY4OTAwMDAwMCwiZXhwIjoxODQ2NzgwMDAwfQ.xxxxxxxxxxxxx
VITE_API_URL=http://localhost:8000
```

**Important Notes:**

- Use the **anon** key for VITE_SUPABASE_ANON_KEY (not the service_role key)
- Frontend uses the anon (public) key for security
- Make sure there are no spaces around the `=` signs

#### Save and Close

---

## Step 7: Verify Setup

Let's make sure everything is working!

### 7.1 Test Database Connection

#### Open Supabase SQL Editor:

- Go back to Supabase dashboard
- Click **"SQL Editor"**

#### Run Test Query:

```sql
-- Test query to count challenges
SELECT COUNT(*) as total_challenges FROM challenges;
```

#### Expected Result:

```
total_challenges: 12
```

#### Run Another Test:

```sql
-- Test query to see challenge categories
SELECT category, COUNT(*) as count
FROM challenges
GROUP BY category;
```

#### Expected Result:

```
Creative Writing              | 3
Coding & Debugging            | 3
Summarization & Rewriting     | 3
Data Extraction               | 3
```

### 7.2 Check Authentication is Enabled

#### Navigate to Authentication:

- Click **"Authentication"** in left sidebar
- Click **"Users"** tab
- You should see an empty user list (that's fine)
- This confirms auth is working

#### Check Policies:

- Click **"Database"** → **"Tables"**
- Click on **"evaluations"** table
- You should see RLS (Row Level Security) is **ENABLED**
- This is correct - it protects user data

### 7.3 Visual Checklist

✅ Project created and fully initialized  
✅ schema.sql ran successfully  
✅ seed.sql ran successfully  
✅ Can see 12 challenges in Table Editor  
✅ Can see both tables (challenges, evaluations)  
✅ Copied all 5 credentials (URL, anon key, service_role key, JWT secret, database URL)  
✅ Updated backend/.env with service_role key  
✅ Updated frontend/.env with anon key  
✅ Test queries return correct results

---

## 🎉 Supabase Setup Complete!

Your Supabase database is now fully configured with:

- ✅ Database tables created
- ✅ 12 sample challenges loaded
- ✅ Row Level Security policies enabled
- ✅ Authentication configured
- ✅ API credentials obtained and configured

---

## 🚀 Next Steps

1. **Get OpenRouter API Key** (see QUICKSTART.md Step 3)
2. **Start your application:**

   ```powershell
   # Terminal 1 - Backend
   cd "d:\Project\prompt analyst"
   .\start-backend.ps1

   # Terminal 2 - Frontend
   .\start-frontend.ps1
   ```

---

## 🔍 Troubleshooting

### "Error: No API Keys Found"

- Make sure you're looking in **Settings** → **API**
- The keys are long strings starting with `eyJ`
- Click "Reveal" buttons to see secret keys

### "Cannot connect to database"

- Verify your database password is correct in DATABASE_URL
- Make sure you replaced `[YOUR-PASSWORD]` with actual password
- Check that project is fully initialized (no loading indicators)

### "Schema already exists" error

- This is okay! It means the schema already ran
- Click **Table Editor** to verify tables exist
- If tables are there, continue to seed.sql

### "Row Level Security" errors

- This is normal and correct
- RLS protects user data
- Your application handles this automatically

### Tables are empty after seed.sql

- Make sure you ran seed.sql AFTER schema.sql
- Check for any error messages when running seed.sql
- Try running seed.sql again

### Need to Start Over?

- Go to **Settings** → **General**
- Scroll to bottom
- Click **"Pause Project"** then **"Delete Project"**
- Create a new project and start from Step 2

---

## 📞 Need More Help?

- **Supabase Documentation**: https://supabase.com/docs
- **Supabase Discord**: https://discord.supabase.com
- **Check Project Settings**: Settings → General → Project Status

---

**Congratulations! Your Supabase database is ready! 🎊**
