# PromptMaster - Project Overview

## 🎯 Project Summary

PromptMaster is a full-stack web application designed to help users improve their prompt engineering skills through interactive challenges, AI-powered evaluation, and detailed progress tracking.

## 📋 Features Implemented

### ✅ User Authentication

- Email/password signup and login via Supabase Auth
- Google OAuth integration ready
- Secure JWT-based authentication
- Protected routes and API endpoints

### ✅ Challenge System

- 12 predefined challenges across 4 categories:
  - Creative Writing (3 challenges)
  - Coding & Debugging (3 challenges)
  - Summarization & Rewriting (3 challenges)
  - Data Extraction (3 challenges)
- Three difficulty levels: Beginner, Intermediate, Advanced
- Filtering by category and difficulty
- Example prompts for each challenge

### ✅ AI Evaluation System

- Real-time prompt evaluation using OpenRouter API
- Scoring on 4 criteria (0-10 scale):
  - **Clarity**: Structure and understandability
  - **Specificity**: Detailed instructions
  - **Creativity**: Unique approach
  - **Relevance**: Goal alignment
- Overall score calculation
- AI-generated output based on user's prompt

### ✅ Improvement Suggestions

- AI-generated specific feedback
- Categorized suggestions (clarity, specificity, creativity, relevance)
- Priority levels (high, medium, low)
- Actionable recommendations stored with each evaluation

### ✅ Progress Tracking

- Dashboard with key metrics:
  - Total attempts
  - Average score
  - Improvement rate
  - Best category
- Detailed history of all evaluations
- Score trends visualization with charts
- Top 3 common mistakes analysis
- Category-specific performance stats

### ✅ User Interface

- Modern, responsive design with TailwindCSS
- Mobile-friendly layout
- Intuitive navigation
- Real-time feedback
- Loading states and error handling
- Dark/light themed components

## 🏗️ Architecture

### Backend (Python FastAPI)

```
backend/
├── app/
│   ├── api/              # API endpoints
│   │   ├── auth.py       # Authentication routes
│   │   ├── challenges.py # Challenge routes
│   │   ├── evaluate.py   # Evaluation routes
│   │   └── progress.py   # Progress tracking routes
│   ├── services/         # Business logic
│   │   ├── auth_service.py
│   │   ├── challenge_service.py
│   │   ├── evaluation_service.py
│   │   └── progress_service.py
│   ├── models/           # Data models
│   │   └── schemas.py
│   ├── core/             # Configuration
│   │   └── config.py
│   └── main.py           # FastAPI application
└── requirements.txt
```

### Frontend (React + Vite)

```
frontend/
├── src/
│   ├── components/       # Reusable components
│   │   └── Layout.jsx
│   ├── pages/           # Page components
│   │   ├── Login.jsx
│   │   ├── Signup.jsx
│   │   ├── Dashboard.jsx
│   │   ├── Challenges.jsx
│   │   ├── Challenge.jsx
│   │   ├── History.jsx
│   │   └── Progress.jsx
│   ├── contexts/        # React Context
│   │   └── AuthContext.jsx
│   ├── services/        # API services
│   │   ├── api.js
│   │   └── supabase.js
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
└── package.json
```

### Database (Supabase PostgreSQL)

```
database/
├── schema.sql           # Database schema
└── seed.sql            # Sample data
```

**Tables:**

- `challenges` - Challenge definitions
- `evaluations` - User submissions and scores
- Row Level Security (RLS) policies enabled

## 🔧 Technology Stack

### Backend

- **FastAPI** - Modern Python web framework
- **Supabase Python Client** - Database and auth
- **httpx** - Async HTTP client for API calls
- **Pydantic** - Data validation
- **OpenRouter API** - AI model access

### Frontend

- **React 18** - UI library
- **React Router** - Navigation
- **TailwindCSS** - Styling
- **Vite** - Build tool
- **Recharts** - Data visualization
- **Axios** - HTTP client
- **Lucide React** - Icons

### Database & Auth

- **Supabase** - PostgreSQL database
- **Supabase Auth** - Authentication service
- **Row Level Security** - Data protection

### AI

- **OpenRouter** - Access to multiple AI models
- **Mistral 7B** - Default model (configurable)

## 📊 Database Schema

### challenges

- id (serial, PK)
- category (varchar)
- title (varchar)
- description (text)
- goal (text)
- example_prompt (text)
- difficulty (varchar)
- created_at (timestamp)

### evaluations

- id (serial, PK)
- user_id (uuid, FK → auth.users)
- challenge_id (int, FK → challenges)
- user_prompt (text)
- ai_output (text)
- clarity_score (decimal)
- specificity_score (decimal)
- creativity_score (decimal)
- relevance_score (decimal)
- overall_score (decimal)
- suggestions (jsonb)
- created_at (timestamp)

## 🔐 Security Features

- JWT-based authentication
- Row Level Security (RLS) policies
- Secure environment variable management
- CORS protection
- Password hashing via Supabase
- API key protection

## 🚀 API Endpoints

### Authentication

- `POST /api/auth/signup` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/google` - Google OAuth
- `GET /api/auth/me` - Get current user
- `POST /api/auth/logout` - Logout user

### Challenges

- `GET /api/challenges` - Get all challenges
- `GET /api/challenges/{id}` - Get specific challenge
- `GET /api/challenges/category/{category}` - Get by category
- `GET /api/challenges/random/challenge` - Get random challenge

### Evaluation

- `POST /api/evaluate` - Submit prompt for evaluation
- `GET /api/evaluate/history` - Get evaluation history
- `GET /api/evaluate/{id}` - Get specific evaluation

### Progress

- `GET /api/progress/dashboard` - Get dashboard stats
- `GET /api/progress/trends` - Get progress trends
- `GET /api/progress/mistakes` - Get top mistakes
- `GET /api/progress/category/{category}` - Get category stats

## 📈 Key Metrics Tracked

1. **Overall Performance**

   - Total attempts
   - Average score
   - Improvement rate
   - Best performing category

2. **Score Trends**

   - Daily average scores
   - Attempts per day
   - 7/30/90 day views

3. **Areas for Improvement**

   - Top 3 most common mistakes
   - Frequency analysis
   - Categorized feedback

4. **Category Performance**
   - Attempts per category
   - Average score per category
   - Best/worst categories

## 🎨 UI Components

- **Dashboard** - Overview with quick stats
- **Challenges** - Browse and filter challenges
- **Challenge Detail** - Complete individual challenges
- **Evaluation Results** - Detailed scoring and feedback
- **History** - Past submissions
- **Progress** - Trends and analytics
- **Authentication** - Login/Signup forms

## 🔄 User Flow

1. User signs up/logs in
2. Views dashboard with stats
3. Browses challenges by category/difficulty
4. Selects a challenge
5. Reads goal and example prompt
6. Writes their own prompt
7. Submits for AI evaluation
8. Receives scores and suggestions
9. Reviews improvement areas
10. Tracks progress over time

## 📝 Configuration

### Environment Variables

**Backend (.env):**

- `SUPABASE_URL`
- `SUPABASE_KEY`
- `SUPABASE_JWT_SECRET`
- `DATABASE_URL`
- `OPENROUTER_API_KEY`

**Frontend (.env):**

- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`
- `VITE_API_URL`

## 🚦 Getting Started

1. **Quick Setup:**

   ```powershell
   .\setup.ps1
   ```

2. **Start Backend:**

   ```powershell
   .\start-backend.ps1
   ```

3. **Start Frontend:**
   ```powershell
   .\start-frontend.ps1
   ```

For detailed instructions, see [SETUP.md](SETUP.md)

## 🎯 Future Enhancements

### Phase 2 Features (Planned)

- [ ] Prompt Coach mode (interactive improvement)
- [ ] User-generated challenges
- [ ] AI skill level estimation
- [ ] Export prompt history
- [ ] Leaderboard system
- [ ] Prompt versioning and comparison
- [ ] Challenge recommendations
- [ ] Achievement badges
- [ ] Social features (share prompts)
- [ ] More AI model options

### Technical Improvements

- [ ] Unit tests for backend
- [ ] Integration tests
- [ ] Frontend testing (Jest/Vitest)
- [ ] CI/CD pipeline
- [ ] Docker containerization
- [ ] Rate limiting
- [ ] Caching layer
- [ ] Advanced analytics

## 📚 Documentation

- [README.md](README.md) - Main documentation
- [SETUP.md](SETUP.md) - Detailed setup guide
- [API Documentation](http://localhost:8000/docs) - Interactive API docs (when running)

## 🤝 Contributing

This is a learning project! Feel free to:

- Add more challenges
- Improve evaluation prompts
- Enhance UI/UX
- Add new features
- Fix bugs
- Improve documentation

## 📄 License

MIT License - Feel free to use this project for learning or building your own applications!

## 🎓 Learning Outcomes

This project demonstrates:

- Full-stack development with Python and React
- RESTful API design
- Database design and management
- Authentication and authorization
- AI API integration
- Modern frontend development
- State management in React
- Responsive design
- Data visualization
- Error handling and validation

## 💡 Tips for Developers

1. **Backend Development:**

   - Use FastAPI's automatic docs at `/docs`
   - Test API endpoints with Swagger UI
   - Check logs for debugging

2. **Frontend Development:**

   - Use React DevTools for debugging
   - Check browser console for errors
   - Hot reload is enabled for fast development

3. **Database:**

   - Use Supabase SQL Editor for queries
   - View data in Supabase Table Editor
   - Monitor API usage in Supabase dashboard

4. **AI Integration:**
   - Test different models in OpenRouter
   - Adjust evaluation prompts in `evaluation_service.py`
   - Monitor API costs in OpenRouter dashboard

---

**Happy Coding! 🚀**
