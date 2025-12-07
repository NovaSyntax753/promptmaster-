# Quick Deployment Guide

## 🚀 Fastest Way to Deploy

### Backend (Railway) - 5 minutes

1. Go to [railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. In settings:
   - **Root Directory**: `backend`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables (see below)
6. Deploy! Get your backend URL

### Frontend (Vercel) - 3 minutes

1. Go to [vercel.com](https://vercel.com) and sign up
2. Click "Add New Project" → Import from GitHub
3. Select your repository
4. Configure:
   - **Root Directory**: `frontend`
   - **Framework Preset**: Vite
5. Add environment variables (see below)
6. Deploy! Get your frontend URL

### Update Backend CORS

Add your Vercel URL to Railway environment variables:
```
FRONTEND_URL=https://your-app.vercel.app
```

---

## 📋 Environment Variables Checklist

### Backend (Railway/Render)

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_service_role_key
SUPABASE_JWT_SECRET=your_jwt_secret
DATABASE_URL=your_database_url
OPENROUTER_API_KEY=your_openrouter_key
FRONTEND_URL=https://your-frontend.vercel.app
ENVIRONMENT=production
```

### Frontend (Vercel/Netlify)

```env
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_anon_key
VITE_API_URL=https://your-backend.railway.app
```

---

## ✅ Post-Deployment

1. Test backend: `https://your-backend-url/health`
2. Test frontend: Visit your Vercel URL
3. Test login/signup
4. Test a challenge submission

---

## 🆘 Common Issues

**CORS Error?**
- Add `FRONTEND_URL` to backend env vars

**API not working?**
- Check `VITE_API_URL` in frontend env vars

**Database error?**
- Verify `DATABASE_URL` format
- Check Supabase connection settings

---

For detailed instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md)




