-- PromptMaster Database Schema
-- Run this in Supabase SQL Editor

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Challenges Table
CREATE TABLE IF NOT EXISTS challenges (
    id SERIAL PRIMARY KEY,
    category VARCHAR(100) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    goal TEXT NOT NULL,
    example_prompt TEXT NOT NULL,
    difficulty VARCHAR(50) NOT NULL CHECK (difficulty IN ('beginner', 'intermediate', 'advanced')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Evaluations Table
CREATE TABLE IF NOT EXISTS evaluations (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    challenge_id INTEGER NOT NULL REFERENCES challenges(id) ON DELETE CASCADE,
    user_prompt TEXT NOT NULL,
    ai_output TEXT NOT NULL,
    clarity_score DECIMAL(4,2) NOT NULL CHECK (clarity_score >= 0 AND clarity_score <= 10),
    specificity_score DECIMAL(4,2) NOT NULL CHECK (specificity_score >= 0 AND specificity_score <= 10),
    creativity_score DECIMAL(4,2) NOT NULL CHECK (creativity_score >= 0 AND creativity_score <= 10),
    relevance_score DECIMAL(4,2) NOT NULL CHECK (relevance_score >= 0 AND relevance_score <= 10),
    overall_score DECIMAL(4,2) NOT NULL CHECK (overall_score >= 0 AND overall_score <= 10),
    suggestions JSONB NOT NULL DEFAULT '[]',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better query performance
CREATE INDEX idx_evaluations_user_id ON evaluations(user_id);
CREATE INDEX idx_evaluations_challenge_id ON evaluations(challenge_id);
CREATE INDEX idx_evaluations_created_at ON evaluations(created_at DESC);
CREATE INDEX idx_challenges_category ON challenges(category);
CREATE INDEX idx_challenges_difficulty ON challenges(difficulty);

-- Row Level Security (RLS) Policies

-- Enable RLS on evaluations table
ALTER TABLE evaluations ENABLE ROW LEVEL SECURITY;

-- Policy: Users can only read their own evaluations
CREATE POLICY "Users can view own evaluations"
    ON evaluations FOR SELECT
    USING (auth.uid() = user_id);

-- Policy: Users can insert their own evaluations
CREATE POLICY "Users can insert own evaluations"
    ON evaluations FOR INSERT
    WITH CHECK (auth.uid() = user_id);

-- Policy: Users can update their own evaluations
CREATE POLICY "Users can update own evaluations"
    ON evaluations FOR UPDATE
    USING (auth.uid() = user_id);

-- Policy: Users can delete their own evaluations
CREATE POLICY "Users can delete own evaluations"
    ON evaluations FOR DELETE
    USING (auth.uid() = user_id);

-- Enable RLS on challenges table (read-only for all authenticated users)
ALTER TABLE challenges ENABLE ROW LEVEL SECURITY;

-- Policy: All authenticated users can read challenges
CREATE POLICY "Authenticated users can view challenges"
    ON challenges FOR SELECT
    TO authenticated
    USING (true);

-- Create a function to get user statistics
CREATE OR REPLACE FUNCTION get_user_statistics(user_uuid UUID)
RETURNS TABLE (
    total_attempts BIGINT,
    average_score DECIMAL,
    best_score DECIMAL,
    improvement_rate DECIMAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        COUNT(*)::BIGINT as total_attempts,
        ROUND(AVG(overall_score)::DECIMAL, 2) as average_score,
        ROUND(MAX(overall_score)::DECIMAL, 2) as best_score,
        CASE
            WHEN COUNT(*) >= 4 THEN
                ROUND(
                    (
                        (AVG(CASE WHEN row_num > (COUNT(*) OVER () / 2) THEN overall_score END) -
                         AVG(CASE WHEN row_num <= (COUNT(*) OVER () / 2) THEN overall_score END)) /
                        AVG(CASE WHEN row_num <= (COUNT(*) OVER () / 2) THEN overall_score END) * 100
                    )::DECIMAL,
                    2
                )
            ELSE 0
        END as improvement_rate
    FROM (
        SELECT
            overall_score,
            ROW_NUMBER() OVER (ORDER BY created_at) as row_num,
            COUNT(*) OVER () as total_count
        FROM evaluations
        WHERE user_id = user_uuid
    ) subquery;
END;
$$ LANGUAGE plpgsql;

-- Create a view for dashboard statistics
CREATE OR REPLACE VIEW user_dashboard_stats AS
SELECT
    e.user_id,
    COUNT(*) as total_attempts,
    ROUND(AVG(e.overall_score)::DECIMAL, 2) as average_score,
    MAX(e.overall_score) as best_score,
    MIN(e.overall_score) as lowest_score,
    COUNT(DISTINCT e.challenge_id) as challenges_attempted,
    COUNT(DISTINCT c.category) as categories_explored
FROM evaluations e
LEFT JOIN challenges c ON e.challenge_id = c.id
GROUP BY e.user_id;

-- Grant necessary permissions
GRANT SELECT ON user_dashboard_stats TO authenticated;
GRANT EXECUTE ON FUNCTION get_user_statistics TO authenticated;
