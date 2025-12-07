# Deployment Guide

This guide will help you deploy the PromptMaster application to production.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Deployment Options](#deployment-options)
3. [Backend Deployment](#backend-deployment)
4. [Frontend Deployment](#frontend-deployment)
5. [Environment Variables](#environment-variables)
6. [Post-Deployment Checklist](#post-deployment-checklist)

## Prerequisites

Before deploying, ensure you have:

- ✅ A Supabase project set up with database schema
- ✅ All environment variables ready
- ✅ GitHub repository (for automated deployments)
- ✅ Accounts on deployment platforms:
  - **Backend**: Railway, Render, or Fly.io
  - **Frontend**: Vercel or Netlify

## Deployment Options

### Recommended Setup

- **Backend**: Railway or Render (easy Python/FastAPI deployment)
- **Frontend**: Vercel (excellent React/Vite support)

### Alternative Options

- **Backend**: Fly.io, Heroku, AWS, Google Cloud
- **Frontend**: Netlify, Cloudflare Pages, AWS Amplify

---

## Backend Deployment

### Option 1: Railway (Recommended)

Railway is the easiest option for FastAPI deployment.

#### Steps:

1. **Sign up** at [railway.app](https://railway.app)

2. **Create a new project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Connect your repository
   - Select the repository

3. **Configure the service**:
   - Railway will auto-detect Python
   - Set the **Root Directory** to `backend`
   - Set the **Start Command** to:
     ```bash
     uvicorn app.main:app --host 0.0.0.0 --port $PORT
     ```

4. **Add Environment Variables**:
   - Go to Variables tab
   - Add all variables from `backend/.env.example`:
     ```
     SUPABASE_URL=your_supabase_url
     SUPABASE_KEY=your_supabase_service_role_key
     SUPABASE_JWT_SECRET=your_jwt_secret
     DATABASE_URL=your_supabase_database_url
     OPENROUTER_API_KEY=your_openrouter_key
     GROQ_API_KEY=your_groq_key (optional)
     ENVIRONMENT=production
     ```

5. **Deploy**:
   - Railway will automatically deploy on push
   - Get your backend URL (e.g., `https://your-app.railway.app`)

6. **Update CORS**:
   - Update `backend/app/core/config.py` to include your frontend URL
   - Or add `FRONTEND_URL` environment variable

### Option 2: Render

1. **Sign up** at [render.com](https://render.com)

2. **Create a new Web Service**:
   - Connect your GitHub repository
   - Select the repository

3. **Configure**:
   - **Name**: `promptmaster-backend`
   - **Environment**: Python 3
   - **Build Command**: `cd backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Root Directory**: `backend`

4. **Add Environment Variables** (same as Railway)

5. **Deploy**: Render will deploy automatically

### Option 3: Docker Deployment

If you prefer Docker, use the included `Dockerfile`:

```bash
# Build the image
docker build -t promptmaster-backend ./backend

# Run the container
docker run -p 8000:8000 --env-file backend/.env promptmaster-backend
```

For production with Docker:
- Use Docker Compose
- Deploy to AWS ECS, Google Cloud Run, or Azure Container Instances

---

## Frontend Deployment

### Option 1: Vercel (Recommended)

Vercel has excellent support for Vite/React apps.

#### Steps:

1. **Sign up** at [vercel.com](https://vercel.com)

2. **Import your project**:
   - Click "Add New Project"
   - Import from GitHub
   - Select your repository

3. **Configure**:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`

4. **Add Environment Variables**:
   ```
   VITE_SUPABASE_URL=your_supabase_url
   VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
   VITE_API_URL=https://your-backend-url.railway.app
   ```

5. **Deploy**:
   - Click "Deploy"
   - Vercel will build and deploy automatically
   - Get your frontend URL (e.g., `https://your-app.vercel.app`)

6. **Update Backend CORS**:
   - Add your Vercel URL to `BACKEND_CORS_ORIGINS` in backend config
   - Or set `FRONTEND_URL` environment variable

### Option 2: Netlify

1. **Sign up** at [netlify.com](https://netlify.com)

2. **Create a new site**:
   - Connect to GitHub
   - Select your repository

3. **Configure build settings**:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/dist`

4. **Add Environment Variables** (same as Vercel)

5. **Deploy**: Netlify will deploy automatically

---

## Environment Variables

### Backend Environment Variables

Create these in your backend deployment platform:

```env
# Required
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_service_role_key
SUPABASE_JWT_SECRET=your_jwt_secret
DATABASE_URL=postgresql://user:password@host:port/dbname

# AI API (at least one required)
OPENROUTER_API_KEY=your_openrouter_key
# OR
GROQ_API_KEY=your_groq_key
# OR
OLLAMA_BASE_URL=http://your-ollama-server:11434
# OR
HUGGINGFACE_API_KEY=your_huggingface_key

# Optional
ENVIRONMENT=production
DEFAULT_MODEL=llama-3.1-8b-instant
EVALUATION_MODEL=llama-3.1-8b-instant
```

### Frontend Environment Variables

Create these in your frontend deployment platform:

```env
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your_anon_key
VITE_API_URL=https://your-backend-url.railway.app
```

**Important**: 
- Vite requires the `VITE_` prefix for environment variables
- These variables are exposed to the browser, so never put secrets here
- Use Supabase's `anon` key, not the `service_role` key

---

## Post-Deployment Checklist

### Backend

- [ ] Backend is accessible at the deployed URL
- [ ] Health check endpoint works: `https://your-backend-url/health`
- [ ] API docs accessible: `https://your-backend-url/docs`
- [ ] CORS is configured correctly
- [ ] Environment variables are set
- [ ] Database connection works
- [ ] Supabase authentication works

### Frontend

- [ ] Frontend is accessible at the deployed URL
- [ ] Can connect to backend API
- [ ] Authentication (login/signup) works
- [ ] All pages load correctly
- [ ] API calls are successful
- [ ] Environment variables are set

### Database

- [ ] Database schema is deployed
- [ ] Seed data is loaded (if needed)
- [ ] Database migrations are applied

### Testing

- [ ] Test user registration
- [ ] Test user login
- [ ] Test challenge fetching
- [ ] Test prompt evaluation
- [ ] Test progress tracking
- [ ] Test all major features

---

## Troubleshooting

### Backend Issues

**Problem**: CORS errors
- **Solution**: Add your frontend URL to `BACKEND_CORS_ORIGINS` in backend config

**Problem**: Database connection fails
- **Solution**: Check `DATABASE_URL` format and credentials

**Problem**: Environment variables not loading
- **Solution**: Ensure all variables are set in deployment platform

### Frontend Issues

**Problem**: API calls fail
- **Solution**: Check `VITE_API_URL` is set correctly

**Problem**: Supabase auth not working
- **Solution**: Verify `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY`

**Problem**: Build fails
- **Solution**: Check Node.js version (should be 18+)

---

## Continuous Deployment

Both Railway and Vercel support automatic deployments:

- **Railway**: Deploys on every push to main branch
- **Vercel**: Deploys on every push (creates preview for PRs)

To disable auto-deploy:
- Railway: Settings → Source → Disable auto-deploy
- Vercel: Project Settings → Git → Disable auto-deploy

---

## Custom Domain Setup

### Backend (Railway)

1. Go to your service settings
2. Click "Generate Domain" or "Custom Domain"
3. Add your domain
4. Update DNS records as instructed

### Frontend (Vercel)

1. Go to Project Settings → Domains
2. Add your domain
3. Update DNS records as instructed
4. SSL certificate is automatically provisioned

---

## Monitoring & Logs

### Railway
- View logs in the Railway dashboard
- Set up alerts in project settings

### Vercel
- View logs in the Vercel dashboard
- Set up analytics in project settings

### Recommended Tools
- **Sentry**: Error tracking
- **LogRocket**: Session replay
- **Uptime Robot**: Uptime monitoring

---

## Security Checklist

- [ ] All secrets are in environment variables (not in code)
- [ ] CORS is properly configured
- [ ] Database credentials are secure
- [ ] API keys are rotated regularly
- [ ] HTTPS is enabled
- [ ] Rate limiting is configured (if needed)

---

## Cost Estimation

### Free Tier Options

- **Railway**: $5/month free credit (usually enough for small apps)
- **Render**: Free tier available (with limitations)
- **Vercel**: Free tier for personal projects
- **Netlify**: Free tier available
- **Supabase**: Free tier with 500MB database

### Paid Options

- **Railway**: Pay-as-you-go after free credit
- **Vercel**: Pro plan starts at $20/month
- **Supabase**: Pro plan starts at $25/month

---

## Need Help?

If you encounter issues:

1. Check the logs in your deployment platform
2. Verify all environment variables are set
3. Test endpoints using the API docs (`/docs`)
4. Check the troubleshooting section above

For more help, refer to:
- [Railway Docs](https://docs.railway.app)
- [Vercel Docs](https://vercel.com/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [Vite Docs](https://vitejs.dev)




