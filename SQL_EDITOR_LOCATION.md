# Where to Run Database Scripts - Visual Guide

## 📍 You Run Scripts in the Supabase SQL Editor

Let me show you step by step with clear directions:

---

## Step-by-Step: Finding the SQL Editor

### 1. Open Supabase Dashboard

- Go to: **https://app.supabase.com**
- Log in to your account
- You'll see your project (PromptMaster)
- **Click on your project name** to open it

### 2. Find the SQL Editor

Look at the **LEFT SIDEBAR** - you'll see a menu with icons and text:

```
🏠 Home
📊 Table Editor
🗄️  Database
    ↳ Tables
    ↳ Triggers
    ↳ Functions
    ↳ Extensions
    ↳ Replication
    ↳ Webhooks
🔐 Authentication
📦 Storage
💾 Backups
⚙️  Settings
```

**Click on "Database"** (looks like a database/cylinder icon)

When you click "Database", it expands to show sub-options:

- Tables
- Triggers
- Functions
- Extensions
- Replication
- Webhooks

**BUT WAIT!** You need the **SQL Editor**, not these options!

### 3. The Correct Location

The **SQL Editor** might be:

**Option A: Separate menu item**

- Look for **"SQL Editor"** as its own item in the left sidebar
- It might have a terminal/code icon (</>)
- Click on it

**Option B: Under Database section**

- After clicking "Database", look for **"SQL Editor"** in the submenu

**Option C: Top navigation**

- Some Supabase versions have SQL Editor at the top
- Look for a tab labeled **"SQL"** or **"SQL Editor"**

**Option D: Direct link**

- Go directly to: `https://app.supabase.com/project/YOUR-PROJECT-ID/sql`

---

## 🎯 Once You're in SQL Editor

You'll see a screen that looks like this:

```
┌─────────────────────────────────────────────────────────────┐
│  SQL Editor                                  [+ New query]  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [Empty editor with blinking cursor]                        │
│                                                              │
│  -- Type your SQL here or paste from file                   │
│                                                              │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  [RUN] button                                               │
└─────────────────────────────────────────────────────────────┘
```

**This is where you paste and run your SQL scripts!**

---

## 📝 Running schema.sql (Step by Step)

### Step 1: Open the SQL file on your computer

```powershell
# Open with Notepad
notepad "d:\Project\prompt analyst\database\schema.sql"
```

### Step 2: Copy the entire file

- Press **Ctrl + A** (select all)
- Press **Ctrl + C** (copy)

### Step 3: Go to Supabase SQL Editor

- In Supabase dashboard
- Click **"SQL Editor"** in left sidebar (or find it using instructions above)
- Click **"+ New query"** button (top right)

### Step 4: Paste and run

- Click in the empty editor area
- Press **Ctrl + V** (paste)
- You should see a LOT of SQL code appear
- Click the **"RUN"** button at the bottom
- Or press **Ctrl + Enter**

### Step 5: Check for success

You should see a message at the bottom:

```
✓ Success. No rows returned
```

If you see errors, don't worry - note them and ask for help!

---

## 📝 Running seed.sql (Step by Step)

### Step 1: Open the SQL file

```powershell
# Open with Notepad
notepad "d:\Project\prompt analyst\database\seed.sql"
```

### Step 2: Copy the entire file

- Press **Ctrl + A** (select all)
- Press **Ctrl + C** (copy)

### Step 3: Create new query in Supabase

- **Still in SQL Editor**
- Click **"+ New query"** button again (top right)
- This creates a fresh, empty query tab

### Step 4: Paste and run

- Click in the empty editor area
- Press **Ctrl + V** (paste)
- You should see all the INSERT statements
- Click the **"RUN"** button at the bottom
- Or press **Ctrl + Enter**

### Step 5: Check for success

You should see:

```
✓ Success. No rows returned
```

---

## ✅ Verify Everything Worked

### Check Tables Were Created

1. In the left sidebar, click **"Table Editor"**
2. You should see a list of tables:

   - **auth** (folder with user tables - created automatically)
   - **challenges** ← You created this!
   - **evaluations** ← You created this!
   - **public** (folder)

3. **Click on "challenges"** table
4. You should see **12 rows** of data with columns:
   - id
   - category
   - title
   - description
   - goal
   - example_prompt
   - difficulty
   - created_at

If you see this, **SUCCESS!** ✅

---

## 🎬 Visual Walkthrough (Text Version)

```
YOU ARE HERE → Supabase Dashboard (app.supabase.com)
    ↓
Click your project (PromptMaster)
    ↓
Look at LEFT SIDEBAR
    ↓
Find and click "SQL Editor"
(might be under "Database" or separate item)
    ↓
Click "+ New query" button
    ↓
Paste schema.sql contents
    ↓
Click "RUN" button
    ↓
See "Success" message ✓
    ↓
Click "+ New query" again
    ↓
Paste seed.sql contents
    ↓
Click "RUN" button
    ↓
See "Success" message ✓
    ↓
Click "Table Editor" in left sidebar
    ↓
See "challenges" and "evaluations" tables ✓
    ↓
Click "challenges" → See 12 rows ✓
    ↓
DONE! 🎉
```

---

## 🔍 Screenshots Guide (Text Description)

### What the SQL Editor Looks Like:

**Top of screen:**

- You'll see: "SQL Editor" as the title
- Green button: "+ New query"
- You might see tabs if you have multiple queries open

**Main area:**

- Large text box (code editor)
- Dark or light background (depends on your theme)
- Line numbers on the left side
- Syntax highlighting (SQL keywords in different colors)

**Bottom of screen:**

- Green "RUN" button (or sometimes blue)
- Might say "Run" or have a play icon ▶
- Results area showing success/error messages
- Might show execution time

---

## ❓ Still Can't Find SQL Editor?

### Try This:

1. **Use the search feature:**

   - Look for a search icon or press **Ctrl + K**
   - Type "SQL" or "SQL Editor"
   - It should appear in the results

2. **Use direct URL:**

   - Get your project ID (from the URL)
   - Go to: `https://app.supabase.com/project/YOUR-PROJECT-ID/sql`
   - Replace YOUR-PROJECT-ID with your actual project ID

3. **Check Supabase version:**

   - If your interface looks different, you might have a newer version
   - Look for any "Query" or "SQL" related menu items
   - Try clicking on "Database" and look for sub-items

4. **Use the quick start guide:**
   - Some Supabase projects show a "Quick Start" guide
   - One of the steps might say "Run a query"
   - Click that to go to SQL Editor

---

## 🆘 Emergency Alternative Method

If you absolutely cannot find the SQL Editor:

### Use Table Editor to Check Setup

1. Click **"Table Editor"** (this one is easy to find!)
2. Click **"+ New table"** button
3. This opens a form, but there's often a **"Use SQL Editor"** link
4. Click that link to go to SQL Editor

---

## 💬 Common Locations by Supabase Version

### Supabase Classic:

- Left sidebar → **"SQL"** or **"SQL Editor"** (direct item)

### Supabase New UI:

- Left sidebar → **"Database"** → Click to expand
- Look for **"SQL Editor"** in the submenu

### Supabase Latest:

- Top navigation bar → **"SQL Editor"** tab
- Or left sidebar → Icon that looks like **</>**

---

## ✅ Quick Checklist

Once you're in the right place, you'll know because:

- [ ] You see a large text area where you can type/paste code
- [ ] There's a "RUN" or play button ▶
- [ ] You can create "New query"
- [ ] The interface looks like a code editor (not a table view)
- [ ] You can see line numbers
- [ ] SQL keywords are highlighted in color

---

## 🎉 Summary

**WHERE:** Supabase Dashboard → SQL Editor (in left sidebar)  
**WHAT:** Paste schema.sql, click RUN, then paste seed.sql, click RUN  
**VERIFY:** Table Editor → See "challenges" table with 12 rows

---

**Need me to explain any step more clearly? Just ask!** 😊
