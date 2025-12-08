import axios from "axios";
import { supabase } from "./supabase";

const API_URL =
  import.meta.env.VITE_API_URL || "https://promptmaster-ou26.onrender.com";

const api = axios.create({
  baseURL: API_URL,
  timeout: 60000, // 60 seconds timeout for Render free tier wake-up
});

// Add auth token to requests
api.interceptors.request.use(async (config) => {
  console.log("API request to:", config.url);
  const {
    data: { session },
  } = await supabase.auth.getSession();
  console.log("Session exists:", !!session);
  if (session?.access_token) {
    config.headers.Authorization = `Bearer ${session.access_token}`;
    console.log("Added auth token to request");
  } else {
    console.log("No session/token found");
  }
  return config;
});

// Challenges API
export const challengesApi = {
  getAll: (params) => api.get("/api/challenges", { params }),
  getById: (id) => api.get(`/api/challenges/${id}`),
  getByCategory: (category) => api.get(`/api/challenges/category/${category}`),
  getRandom: (category) =>
    api.get("/api/challenges/random/challenge", { params: { category } }),
};

// Evaluation API
export const evaluationApi = {
  submit: (data) => api.post("/api/evaluate", data),
  getHistory: (params) => api.get("/api/evaluate/history", { params }),
  getById: (id) => api.get(`/api/evaluate/${id}`),
};

// Progress API
export const progressApi = {
  getDashboard: () => api.get("/api/progress/dashboard"),
  getTrends: (days) => api.get("/api/progress/trends", { params: { days } }),
  getMistakes: () => api.get("/api/progress/mistakes"),
  getCategoryStats: (category) => api.get(`/api/progress/category/${category}`),
};

export default api;
