# PromptMaster Complete File Structure

```
d:\Project\prompt analyst\
│
├── 📁 backend/                                # Python FastAPI Backend
│   ├── 📁 app/
│   │   ├── 📁 api/                           # API Route Handlers
│   │   │   ├── __init__.py                   # Package initializer
│   │   │   ├── auth.py                       # Authentication routes
│   │   │   ├── challenges.py                 # Challenge CRUD routes
│   │   │   ├── evaluate.py                   # Evaluation routes
│   │   │   └── progress.py                   # Progress tracking routes
│   │   │
│   │   ├── 📁 core/                          # Core Configuration
│   │   │   ├── __init__.py
│   │   │   └── config.py                     # Settings & environment vars
│   │   │
│   │   ├── 📁 models/                        # Data Models
│   │   │   ├── __init__.py
│   │   │   └── schemas.py                    # Pydantic models
│   │   │
│   │   ├── 📁 services/                      # Business Logic
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py              # Auth business logic
│   │   │   ├── challenge_service.py         # Challenge logic
│   │   │   ├── evaluation_service.py        # AI evaluation logic
│   │   │   └── progress_service.py          # Analytics logic
│   │   │
│   │   ├── __init__.py
│   │   └── main.py                          # FastAPI application entry
│   │
│   ├── 📁 venv/                              # Python virtual environment
│   │   └── ...                               # (created by setup script)
│   │
│   ├── .env                                  # Environment variables (create this)
│   ├── .env.example                          # Environment template
│   ├── .gitignore                            # Git ignore rules
│   └── requirements.txt                      # Python dependencies
│
├── 📁 frontend/                              # React Frontend Application
│   ├── 📁 public/                            # Static assets
│   │   └── vite.svg                          # Default Vite logo
│   │
│   ├── 📁 src/
│   │   ├── 📁 components/                    # Reusable Components
│   │   │   └── Layout.jsx                    # Main layout with navbar
│   │   │
│   │   ├── 📁 contexts/                      # React Contexts
│   │   │   └── AuthContext.jsx              # Authentication state
│   │   │
│   │   ├── 📁 pages/                         # Page Components
│   │   │   ├── Challenge.jsx                # Single challenge page
│   │   │   ├── Challenges.jsx               # Challenge browser
│   │   │   ├── Dashboard.jsx                # User dashboard
│   │   │   ├── History.jsx                  # Evaluation history
│   │   │   ├── Login.jsx                    # Login page
│   │   │   ├── Progress.jsx                 # Progress analytics
│   │   │   └── Signup.jsx                   # Registration page
│   │   │
│   │   ├── 📁 services/                      # API Services
│   │   │   ├── api.js                        # Axios HTTP client
│   │   │   └── supabase.js                   # Supabase client
│   │   │
│   │   ├── App.jsx                           # Root component
│   │   ├── index.css                         # Global styles (Tailwind)
│   │   └── main.jsx                          # React entry point
│   │
│   ├── 📁 node_modules/                      # Node dependencies
│   │   └── ...                               # (created by npm install)
│   │
│   ├── .env                                  # Environment variables (create this)
│   ├── .env.example                          # Environment template
│   ├── .gitignore                            # Git ignore rules
│   ├── index.html                            # HTML entry point
│   ├── package.json                          # Node dependencies & scripts
│   ├── postcss.config.js                     # PostCSS configuration
│   ├── tailwind.config.js                    # Tailwind CSS config
│   └── vite.config.js                        # Vite build config
│
├── 📁 database/                              # Database Scripts
│   ├── schema.sql                            # Database schema (tables, indexes, RLS)
│   └── seed.sql                              # Sample data (12 challenges)
│
├── 📄 .gitignore                             # Root git ignore
├── 📄 ARCHITECTURE.md                        # Architecture diagrams & data flow
├── 📄 CHECKLIST.md                           # Complete setup checklist
├── 📄 PROJECT_OVERVIEW.md                    # Technical overview & features
├── 📄 QUICKSTART.md                          # Quick start guide
├── 📄 README.md                              # Main documentation
├── 📄 SETUP.md                               # Detailed setup instructions
├── 📄 setup.ps1                              # Automated setup script
├── 📄 start-backend.ps1                      # Start backend server script
└── 📄 start-frontend.ps1                     # Start frontend server script
```

## File Counts by Type

### Backend Files

- **Python Files**: 13 files
  - Route handlers: 4 files (auth, challenges, evaluate, progress)
  - Services: 4 files (auth, challenge, evaluation, progress)
  - Models: 1 file (schemas)
  - Config: 1 file (settings)
  - Entry: 1 file (main)
  - Init files: 5 files

### Frontend Files

- **JSX/JS Files**: 13 files

  - Pages: 7 files (login, signup, dashboard, challenges, challenge, history, progress)
  - Components: 1 file (layout)
  - Services: 2 files (api, supabase)
  - Contexts: 1 file (auth)
  - App files: 2 files (App, main)

- **Configuration Files**: 5 files
  - Vite config
  - Tailwind config
  - PostCSS config
  - Package.json
  - Index.html

### Database Files

- **SQL Scripts**: 2 files
  - Schema definition
  - Seed data

### Documentation Files

- **Markdown Files**: 6 files
  - README
  - SETUP
  - QUICKSTART
  - PROJECT_OVERVIEW
  - ARCHITECTURE
  - CHECKLIST

### Scripts

- **PowerShell Scripts**: 3 files
  - Setup automation
  - Backend starter
  - Frontend starter

### Configuration Files

- **Environment**: 4 templates/files

  - Backend .env.example
  - Frontend .env.example
  - Backend .env (to create)
  - Frontend .env (to create)

- **Git**: 3 files
  - Root .gitignore
  - Backend .gitignore
  - Frontend .gitignore

## Total Files: ~50+ files

## Key Directories Explained

### `/backend/app/api/`

Contains all HTTP endpoint definitions. Each file maps to a route group:

- Routes receive HTTP requests
- Validate input data
- Call service layer
- Return JSON responses

### `/backend/app/services/`

Business logic layer. Services handle:

- Database operations
- External API calls (Supabase, OpenRouter)
- Data processing
- Complex calculations

### `/backend/app/models/`

Pydantic models for data validation:

- Request/response schemas
- Type checking
- Automatic API documentation

### `/frontend/src/pages/`

Full-page React components:

- Each corresponds to a route
- Manages page-level state
- Calls API services
- Renders UI

### `/frontend/src/components/`

Reusable UI components:

- Layout wrapper with navbar
- Can add more shared components

### `/frontend/src/services/`

API communication layer:

- Axios client with interceptors
- Supabase client setup
- Automatic token injection

### `/database/`

SQL scripts for Supabase:

- `schema.sql`: Define tables, indexes, RLS policies, views
- `seed.sql`: Insert sample challenge data

## Files You Need to Create

After running `setup.ps1`, you need to manually create and configure:

1. ✏️ `backend/.env` - Backend environment variables
2. ✏️ `frontend/.env` - Frontend environment variables

Both have `.env.example` templates to copy from.

## Files Generated by Tools

These are created automatically and should NOT be edited:

- ❌ `backend/venv/` - Python virtual environment
- ❌ `frontend/node_modules/` - Node packages
- ❌ `backend/__pycache__/` - Python bytecode cache
- ❌ `frontend/dist/` - Production build output

## Most Important Files to Know

### For Development:

1. 🎯 `backend/app/main.py` - Backend entry point
2. 🎯 `frontend/src/App.jsx` - Frontend entry point
3. 🎯 `backend/app/services/evaluation_service.py` - AI evaluation logic
4. 🎯 `frontend/src/pages/Challenge.jsx` - Challenge interaction

### For Configuration:

1. ⚙️ `backend/.env` - Backend secrets
2. ⚙️ `frontend/.env` - Frontend config
3. ⚙️ `backend/app/core/config.py` - Backend settings
4. ⚙️ `frontend/tailwind.config.js` - UI styling

### For Understanding:

1. 📖 `README.md` - Project overview
2. 📖 `SETUP.md` - Setup instructions
3. 📖 `ARCHITECTURE.md` - System design
4. 📖 `CHECKLIST.md` - Setup verification

## File Relationships

```
main.py
  └─ imports routes from api/
      └─ routes call services/
          └─ services use models/
              └─ models define data structure
                  └─ used by frontend via API

App.jsx
  └─ renders pages/
      └─ pages use services/
          └─ services call backend API
              └─ backend returns data
                  └─ pages display data

schema.sql → Supabase Database ← seed.sql
     ↑                              ↓
     └─ services query database ────┘
```

## Development Workflow

```
1. Edit backend code → backend/ files
2. Backend auto-reloads (uvicorn --reload)
3. Edit frontend code → frontend/src/ files
4. Frontend hot-reloads (Vite HMR)
5. Changes reflected immediately in browser
```

That's the complete file structure! All 50+ files working together to create PromptMaster. 🚀
