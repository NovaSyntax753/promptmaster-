# PromptMaster – Test & Improve Your Prompting Skills

A web application that helps users test their prompt engineering skills, get instant feedback, and learn how to write better prompts.

## Features

- 🔐 **User Authentication** via Supabase (Email + Google OAuth)
- 📝 **Prompt Challenges** across multiple categories
- 🤖 **AI-Powered Evaluation** with detailed scoring
- 💡 **Improvement Suggestions** for better prompts
- 📊 **Progress Tracking** and analytics dashboard
- 📈 **Performance Insights** with graphs and trends

## Tech Stack

- **Frontend**: React + TailwindCSS + Vite
- **Backend**: Python FastAPI
- **Database**: Supabase (PostgreSQL)
- **Authentication**: Supabase Auth
- **AI API**: OpenRouter / Ollama / Hugging Face

## Project Structure

```
prompt-analyst/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── core/           # Configuration
│   │   ├── models/         # Data models
│   │   ├── services/       # Business logic
│   │   └── main.py         # FastAPI app entry
│   ├── requirements.txt
│   └── .env.example
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── services/      # API services
│   │   ├── hooks/         # Custom hooks
│   │   └── App.jsx
│   ├── package.json
│   └── .env.example
├── database/              # Database setup
│   ├── schema.sql        # Database schema
│   └── seed.sql          # Sample data
└── README.md
```

## Setup Instructions

### Prerequisites

- Node.js 18+
- Python 3.9+
- Supabase account
- OpenRouter API key (or Ollama/Hugging Face)

### 1. Clone and Setup

```bash
cd "d:\Project\prompt analyst"
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env` file in backend directory:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SUPABASE_JWT_SECRET=your_jwt_secret
OPENROUTER_API_KEY=your_openrouter_key
DATABASE_URL=your_database_url
```

Run backend:

```bash
uvicorn app.main:app --reload --port 8000
```

### 3. Frontend Setup

```bash
cd frontend
npm install
```

Create `.env` file in frontend directory:

```env
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
VITE_API_URL=http://localhost:8000
```

Run frontend:

```bash
npm run dev
```

### 4. Database Setup

1. Create a new Supabase project
2. Run the SQL from `database/schema.sql` in Supabase SQL Editor
3. (Optional) Run `database/seed.sql` for sample challenges

## Environment Variables

### Backend (.env)

- `SUPABASE_URL`: Your Supabase project URL
- `SUPABASE_KEY`: Your Supabase service role key
- `SUPABASE_JWT_SECRET`: JWT secret from Supabase
- `OPENROUTER_API_KEY`: OpenRouter API key
- `DATABASE_URL`: PostgreSQL connection string

### Frontend (.env)

- `VITE_SUPABASE_URL`: Your Supabase project URL
- `VITE_SUPABASE_ANON_KEY`: Your Supabase anonymous key
- `VITE_API_URL`: Backend API URL (default: http://localhost:8000)

## API Endpoints

### Authentication

- `POST /api/auth/signup` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user

### Challenges

- `GET /api/challenges` - Get all challenges
- `GET /api/challenges/{id}` - Get challenge by ID
- `GET /api/challenges/category/{category}` - Get challenges by category

### Evaluations

- `POST /api/evaluate` - Submit prompt for evaluation
- `GET /api/evaluate/history` - Get user's evaluation history

### Progress

- `GET /api/progress/dashboard` - Get dashboard statistics
- `GET /api/progress/trends` - Get improvement trends
- `GET /api/progress/mistakes` - Get top 3 common mistakes

## Challenge Categories

1. **Creative Writing** - Storytelling, content creation
2. **Coding & Debugging** - Code generation, problem-solving
3. **Summarization & Rewriting** - Text condensation, paraphrasing
4. **Data Extraction** - Information extraction, structured output

## Scoring Criteria

Each prompt is evaluated on 4 metrics (0-10 scale):

1. **Clarity**: How understandable and structured the prompt is
2. **Specificity**: Whether it provides clear instructions
3. **Creativity**: How unique or interesting the approach is
4. **Relevance**: How well it matches the challenge's goal

**Overall Score**: Average of all four metrics

## Development

### Backend Development

```bash
cd backend
.\venv\Scripts\activate
uvicorn app.main:app --reload
```

### Frontend Development

```bash
cd frontend
npm run dev
```

### Run Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## Deployment

### Backend (Railway/Render)

1. Push code to GitHub
2. Connect repository to Railway/Render
3. Add environment variables
4. Deploy

### Frontend (Vercel/Netlify)

1. Push code to GitHub
2. Connect repository to Vercel/Netlify
3. Add environment variables
4. Deploy

## Future Enhancements

- 🎓 "Prompt Coach" mode (interactive improvement loop)
- 👥 User-generated challenges
- 🎯 AI-based skill level estimation
- 📤 Export prompt history
- 🏆 Leaderboard system
- 🔄 Prompt versioning and comparison

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
