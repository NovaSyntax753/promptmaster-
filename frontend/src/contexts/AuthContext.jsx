import { createContext, useContext, useState, useEffect } from "react";
import { supabase } from "../services/supabase";

const AuthContext = createContext({});

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check active session
    supabase.auth
      .getSession()
      .then(({ data: { session }, error }) => {
        if (error) {
          console.error("Error getting session:", error);
          // Don't fail completely, just log the error
        }
        setUser(session?.user ?? null);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to get session:", err);
        // Check if it's a configuration error
        if (err.message && err.message.includes("Missing Supabase")) {
          console.error(
            "❌ Missing Supabase environment variables. Please create frontend/.env file."
          );
        }
        setLoading(false);
      });

    // Listen for auth changes
    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange(async (event, session) => {
      setUser(session?.user ?? null);
      setLoading(false);
    });

    return () => subscription.unsubscribe();
  }, []);

  const signUp = async (email, password, fullName) => {
    const { data, error } = await supabase.auth.signUp({
      email,
      password,
      options: {
        data: {
          full_name: fullName,
        },
        emailRedirectTo: window.location.origin,
      },
    });

    if (error) throw error;
    return data;
  };

  const signIn = async (email, password) => {
    try {
      const { data, error } = await supabase.auth.signInWithPassword({
        email,
        password,
      });

      if (error) {
        // Provide more helpful error messages
        if (
          error.message.includes("Failed to fetch") ||
          error.message.includes("Network")
        ) {
          throw new Error(
            "Cannot connect to Supabase. Please check your internet connection and ensure the Supabase credentials are configured in the .env file."
          );
        }
        if (error.message.includes("Invalid login credentials")) {
          throw new Error(
            "Invalid email or password. Please check your credentials and try again."
          );
        }
        if (error.message.includes("Email not confirmed")) {
          throw new Error(
            "Please check your email and confirm your account before signing in."
          );
        }
        throw error;
      }
      return data;
    } catch (err) {
      // Catch network errors and provide helpful messages
      if (err.message === "Failed to fetch" || err.message.includes("fetch")) {
        const errorMsg =
          "Connection failed. This usually means:\n" +
          "1. Missing Supabase credentials in frontend/.env file\n" +
          "2. Check your internet connection\n" +
          "3. Verify your Supabase project is active";
        throw new Error(errorMsg);
      }
      throw err;
    }
  };

  const signInWithGoogle = async () => {
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider: "google",
      options: {
        redirectTo: window.location.origin,
      },
    });

    if (error) throw error;
    return data;
  };

  const signOut = async () => {
    const { error } = await supabase.auth.signOut();
    if (error) throw error;
  };

  const value = {
    user,
    loading,
    signUp,
    signIn,
    signInWithGoogle,
    signOut,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
