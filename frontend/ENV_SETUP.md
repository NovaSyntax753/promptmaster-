# 🔧 Frontend Environment Setup

## Issue: "Failed to fetch" Error

If you're seeing a "failed to fetch" error when trying to login, it's because the frontend is missing the Supabase credentials in the `.env` file.

## Quick Fix

1. **Create a `.env` file** in the `frontend` directory with the following content:

```env
VITE_SUPABASE_URL=https://your-project-id.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-public-key-here
VITE_API_URL=http://localhost:8000
```

2. **Get your Supabase credentials:**
   - Go to https://supabase.com/dashboard
   - Select your project
   - Go to **Project Settings** > **API**
   - Copy the **Project URL** → use as `VITE_SUPABASE_URL`
   - Copy the **anon public** key (NOT service_role) → use as `VITE_SUPABASE_ANON_KEY`

3. **Restart the frontend server** after creating/updating the `.env` file:
   - Stop the current frontend server (Ctrl+C in its window)
   - Run `npm run dev` again

## Verify Setup

After creating the `.env` file:
1. Restart the frontend dev server
2. Open your browser's developer console (F12)
3. You should NOT see "Missing Supabase environment variables" error
4. Try logging in again

## Still Having Issues?

- Make sure both backend and frontend servers are running
- Check the browser console for specific error messages
- Verify your Supabase project is active and accessible
- Ensure you're using the **anon** key (not service_role) for the frontend



