import { createClient } from "@supabase/supabase-js";

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
  const missingVars = [];
  if (!supabaseUrl) missingVars.push("VITE_SUPABASE_URL");
  if (!supabaseAnonKey) missingVars.push("VITE_SUPABASE_ANON_KEY");

  console.error(
    "❌ Missing Supabase environment variables:",
    missingVars.join(", ")
  );
  console.error("📝 Please create a .env file in the frontend directory with:");
  console.error("   VITE_SUPABASE_URL=your_supabase_url");
  console.error("   VITE_SUPABASE_ANON_KEY=your_supabase_anon_key");
  console.error("   VITE_API_URL=http://localhost:8000");
  console.error("");
  console.error(
    "See CREDENTIALS_SETUP.md or SUPABASE_SETUP.md for instructions."
  );

  throw new Error(
    `Missing Supabase environment variables: ${missingVars.join(
      ", "
    )}. Please create a .env file in the frontend directory.`
  );
}

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
