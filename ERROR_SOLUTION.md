# 🔧 Error Solutions Guide

This document explains the errors you're seeing and how to fix them.

---

## Error 1: "Failed to fetch" on Login Page

### ❌ **What's Happening:**
When you try to log in, you see a red error banner saying **"Failed to fetch"**. This means the frontend cannot connect to Supabase (your authentication service).

### 🔍 **Why It's Happening:**
The frontend is missing the Supabase credentials configuration file (`.env`). Without these credentials, the app doesn't know where to connect.

### ✅ **How to Fix It:**

#### **Option 1: Use the Setup Script (Easiest)**

1. Open PowerShell in your project folder
2. Run this command:
   ```powershell
   .\setup-frontend-env.ps1
   ```
3. Follow the prompts to enter your Supabase credentials
4. Restart your frontend server

#### **Option 2: Create the File Manually**

1. **Create a file** named `.env` in the `frontend` folder:
   ```
   frontend/.env
   ```

2. **Add this content** (replace with your actual values):
   ```env
   VITE_SUPABASE_URL=https://your-project-id.supabase.co
   VITE_SUPABASE_ANON_KEY=your-anon-public-key-here
   VITE_API_URL=http://localhost:8000
   ```

3. **Get your Supabase credentials:**
   - Go to https://supabase.com/dashboard
   - Select your project (or create a new one)
   - Click **Project Settings** (gear icon)
   - Click **API** in the left sidebar
   - Copy the **Project URL** → paste as `VITE_SUPABASE_URL`
   - Copy the **anon public** key (NOT service_role) → paste as `VITE_SUPABASE_ANON_KEY`

4. **Save the file** and **restart your frontend server:**
   - Press `Ctrl+C` in the frontend PowerShell window
   - Run `npm run dev` again

#### **Verify It's Fixed:**
- ✅ The error message should disappear
- ✅ You should be able to log in
- ✅ Check the browser console (F12) - no "Missing Supabase" errors

---

## Error 2: jQuery SyntaxError in DevTools

### ❌ **What's Happening:**
In Chrome DevTools, you see this error:
```
SyntaxError: '*,:x' is not a valid selector.
```
This error appears in `jquery-3.1.1.min.js` (from a browser extension).

### 🔍 **Why It's Happening:**
A **browser extension** (like "Adobe Acrobat: PDF edit, convert, sign tools") is injecting jQuery into your page. The extension's jQuery code has a bug with an invalid CSS selector.

### ✅ **How to Fix It:**

#### **Solution 1: Ignore It (Recommended)**
This error **does NOT affect your application**. It's just noise from a browser extension. You can safely ignore it.

**To hide it in DevTools:**
1. Open Chrome DevTools (F12)
2. Go to **Sources** tab
3. Uncheck **"Pause on uncaught exceptions"** and **"Pause on caught exceptions"**
4. The error will still appear but won't pause execution

#### **Solution 2: Disable the Extension**
If the error is annoying:

1. Go to `chrome://extensions/` in your browser
2. Find the **Adobe Acrobat** extension (or similar)
3. Click the toggle to disable it
4. Refresh your page

**Note:** I've already added code to suppress these errors, so they shouldn't affect your app anymore.

#### **Solution 3: Use Incognito Mode**
Extensions are often disabled in incognito mode:
- Press `Ctrl+Shift+N` to open an incognito window
- Open your app there
- Extensions won't interfere

---

## Quick Checklist

To get your app working:

- [ ] **Backend server is running** at `http://localhost:8000`
- [ ] **Frontend server is running** at `http://localhost:5173`
- [ ] **Frontend `.env` file exists** with Supabase credentials
- [ ] **Backend `.env` file exists** with Supabase credentials
- [ ] **Supabase project is active** and accessible
- [ ] **Internet connection is working**

---

## Still Having Issues?

### Check the Backend
1. Open `http://localhost:8000/health` in your browser
2. You should see: `{"status": "healthy"}`

### Check the Frontend
1. Open `http://localhost:5173` in your browser
2. Open DevTools Console (F12)
3. Look for specific error messages

### Common Issues:

**"Missing Supabase environment variables"**
- → Create/check `frontend/.env` file
- → Make sure variables start with `VITE_`

**"Cannot connect to Supabase"**
- → Check your internet connection
- → Verify Supabase URL is correct
- → Check if your Supabase project is paused (free tier pauses after inactivity)

**"Invalid login credentials"**
- → Make sure you've created an account first (use Sign Up)
- → Check email/password spelling

---

## Need More Help?

1. Check `CREDENTIALS_SETUP.md` for detailed credential setup
2. Check `SUPABASE_SETUP.md` for Supabase project setup
3. Check `frontend/ENV_SETUP.md` for frontend environment setup

---

## Summary

1. **"Failed to fetch"** = Missing Supabase credentials → Create `frontend/.env` file
2. **jQuery error** = Browser extension issue → Ignore it or disable the extension

The jQuery error won't break your app, but the "Failed to fetch" error will. Fix the `.env` file first! 🚀


