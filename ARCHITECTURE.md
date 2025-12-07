# PromptMaster Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                           USER BROWSER                                      │
│                     http://localhost:5173                                   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │  REACT FRONTEND (Vite + TailwindCSS)                                │  │
│  │                                                                       │  │
│  │  Pages:          Components:       Services:                        │  │
│  │  - Login         - Layout          - api.js                         │  │
│  │  - Signup        - Navbar          - supabase.js                    │  │
│  │  - Dashboard                                                         │  │
│  │  - Challenges    Contexts:                                          │  │
│  │  - Challenge     - AuthContext                                      │  │
│  │  - History                                                           │  │
│  │  - Progress                                                          │  │
│  │                                                                       │  │
│  └───────────────────────────┬───────────────────────────────────────────┘  │
│                              │                                              │
└──────────────────────────────┼──────────────────────────────────────────────┘
                               │ HTTP Requests (Axios)
                               │ JWT Token in Headers
                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                      FASTAPI BACKEND                                        │
│                  http://localhost:8000                                      │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │  API Routes (app/api/):                                             │  │
│  │                                                                       │  │
│  │  auth.py          challenges.py    evaluate.py      progress.py     │  │
│  │  - /signup        - GET /          - POST /         - /dashboard    │  │
│  │  - /login         - GET /{id}      - GET /history   - /trends       │  │
│  │  - /google        - /category/{c}  - GET /{id}      - /mistakes     │  │
│  │  - /me            - /random                          - /category/{c} │  │
│  │  - /logout                                                           │  │
│  │                                                                       │  │
│  │  ─────────────────────────────────────────────────────────────────  │  │
│  │                                                                       │  │
│  │  Services (app/services/):                                          │  │
│  │                                                                       │  │
│  │  auth_service.py                 evaluation_service.py              │  │
│  │  - Sign up/in/out               - Submit prompt                     │  │
│  │  - Google OAuth                 - Call AI APIs                      │  │
│  │  - Get user info                - Calculate scores                  │  │
│  │                                  - Generate suggestions              │  │
│  │  challenge_service.py                                               │  │
│  │  - Get challenges               progress_service.py                 │  │
│  │  - Filter/search                - Calculate stats                   │  │
│  │                                  - Analyze trends                    │  │
│  │                                                                       │  │
│  └─────────────────┬───────────────────────┬───────────────────────────┘  │
│                    │                       │                              │
└────────────────────┼───────────────────────┼──────────────────────────────┘
                     │                       │
                     │                       │ HTTPS API Calls
                     │                       │
        ┌────────────▼──────────┐   ┌────────▼─────────────┐
        │                       │   │                      │
        │   SUPABASE            │   │   OPENROUTER AI      │
        │   (PostgreSQL)        │   │   API                │
        │                       │   │                      │
        │  Tables:              │   │  Models:             │
        │  - auth.users         │   │  - Mistral 7B        │
        │  - challenges         │   │  - Llama 3           │
        │  - evaluations        │   │  - GPT-4 (optional)  │
        │                       │   │                      │
        │  Features:            │   │  Features:           │
        │  - Auth service       │   │  - Generate output   │
        │  - Row Level Security │   │  - Evaluate quality  │
        │  - Real-time subs     │   │  - Give suggestions  │
        │                       │   │                      │
        └───────────────────────┘   └──────────────────────┘
```

## Data Flow Example: Submitting a Prompt

```
1. USER ACTION
   │
   └─▶ User writes prompt and clicks "Submit"
       │
       │
2. FRONTEND (Challenge.jsx)
   │
   ├─▶ handleSubmit() called
   │
   ├─▶ evaluationApi.submit() called with:
   │   - challenge_id: 1
   │   - user_prompt: "Write a story about..."
   │
   └─▶ HTTP POST to /api/evaluate
       Headers: { Authorization: "Bearer <jwt_token>" }
       │
       │
3. BACKEND (evaluate.py)
   │
   ├─▶ Route receives request
   │
   ├─▶ Extract token from header
   │
   └─▶ Call evaluation_service.evaluate_prompt()
       │
       │
4. EVALUATION SERVICE
   │
   ├─▶ Validate user token with Supabase
   │
   ├─▶ Fetch challenge details from database
   │
   ├─▶ Call OpenRouter API #1:
   │   Generate AI output using user's prompt
   │   Response: "Once upon a time..."
   │
   ├─▶ Call OpenRouter API #2:
   │   Evaluate prompt quality
   │   Response: { clarity: 8.5, specificity: 7.0, ... }
   │
   ├─▶ Call OpenRouter API #3:
   │   Generate improvement suggestions
   │   Response: [{ category: "clarity", suggestion: "..." }]
   │
   ├─▶ Calculate overall score
   │
   ├─▶ Store in Supabase evaluations table:
   │   - user_id, challenge_id, prompt, output
   │   - all scores, suggestions, timestamp
   │
   └─▶ Return evaluation result
       │
       │
5. FRONTEND RECEIVES RESPONSE
   │
   ├─▶ Update component state
   │
   ├─▶ Display results:
   │   - Overall score badge
   │   - Score breakdown (4 metrics)
   │   - AI generated output
   │   - Improvement suggestions
   │
   └─▶ User can retry or try next challenge
```

## Database Schema Visual

```
┌─────────────────────────────────┐
│        auth.users               │
│  (Managed by Supabase Auth)     │
├─────────────────────────────────┤
│ • id (uuid) PK                  │
│ • email                         │
│ • encrypted_password            │
│ • created_at                    │
│ • user_metadata (full_name)     │
└───────────┬─────────────────────┘
            │
            │ user_id (FK)
            ▼
┌─────────────────────────────────┐     ┌──────────────────────────────┐
│      evaluations                │     │        challenges            │
├─────────────────────────────────┤     ├──────────────────────────────┤
│ • id (serial) PK                │     │ • id (serial) PK             │
│ • user_id (uuid) FK             │◀────│ • category                   │
│ • challenge_id (int) FK         │     │ • title                      │
│ • user_prompt (text)            │     │ • description                │
│ • ai_output (text)              │     │ • goal                       │
│ • clarity_score (decimal)       │     │ • example_prompt             │
│ • specificity_score (decimal)   │     │ • difficulty                 │
│ • creativity_score (decimal)    │     │ • created_at                 │
│ • relevance_score (decimal)     │     └──────────────────────────────┘
│ • overall_score (decimal)       │              ▲
│ • suggestions (jsonb)           │              │
│ • created_at (timestamp)        │              │ challenge_id (FK)
└─────────────────────────────────┘──────────────┘

RLS Policies Applied:
✓ Users can only view/modify their own evaluations
✓ All authenticated users can read challenges
```

## Authentication Flow

```
┌──────────┐
│  SIGNUP  │
└────┬─────┘
     │
     ├─▶ Frontend: useAuth().signUp(email, password, name)
     │
     ├─▶ Supabase Auth: Create user account
     │   - Hash password
     │   - Generate user ID
     │   - Store user_metadata
     │
     ├─▶ Return: { user, session }
     │   - Access token (JWT)
     │   - Refresh token
     │
     └─▶ Frontend: Store user in AuthContext
         Redirect to dashboard

┌──────────┐
│  LOGIN   │
└────┬─────┘
     │
     ├─▶ Frontend: useAuth().signIn(email, password)
     │
     ├─▶ Supabase Auth: Verify credentials
     │   - Check email exists
     │   - Verify password hash
     │
     ├─▶ Return: { user, session }
     │   - New access token
     │
     └─▶ Frontend: Store user in AuthContext
         Redirect to dashboard

┌──────────────────┐
│  AUTHENTICATED   │
│     REQUEST      │
└────┬─────────────┘
     │
     ├─▶ Frontend: api.js interceptor adds token
     │   Headers: { Authorization: "Bearer <token>" }
     │
     ├─▶ Backend: Receives request with token
     │
     ├─▶ auth_service.get_user(token)
     │   - Verify JWT signature
     │   - Check expiration
     │   - Extract user_id
     │
     └─▶ Process request with user_id
         Return protected data
```

## Component Hierarchy

```
App.jsx
│
├─▶ AuthProvider (Context)
│   │
│   └─▶ Router
│       │
│       ├─▶ Public Routes
│       │   ├─▶ /login → Login.jsx
│       │   └─▶ /signup → Signup.jsx
│       │
│       └─▶ Protected Routes (ProtectedRoute wrapper)
│           │
│           └─▶ Layout.jsx
│               ├─▶ Navbar
│               ├─▶ Outlet (nested routes)
│               │   ├─▶ / → Dashboard.jsx
│               │   ├─▶ /challenges → Challenges.jsx
│               │   ├─▶ /challenges/:id → Challenge.jsx
│               │   ├─▶ /history → History.jsx
│               │   └─▶ /progress → Progress.jsx
│               │
│               └─▶ Footer
```

This visual guide should help you understand how all the pieces fit together!
