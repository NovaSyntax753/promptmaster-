import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import { challengesApi, evaluationApi } from "../services/api";
import {
  BookOpen,
  Lightbulb,
  Send,
  ArrowLeft,
  CheckCircle,
  AlertCircle,
  TrendingUp,
  Sparkles,
} from "lucide-react";

const Challenge = () => {
  const { id } = useParams();
  const [challenge, setChallenge] = useState(null);
  const [userPrompt, setUserPrompt] = useState("");
  const [evaluation, setEvaluation] = useState(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchChallenge();
  }, [id]);

  const fetchChallenge = async () => {
    try {
      setLoading(true);
      const response = await challengesApi.getById(id);
      setChallenge(response.data);
    } catch (err) {
      setError("Failed to load challenge");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!userPrompt.trim()) return;

    try {
      setSubmitting(true);
      setError("");
      const response = await evaluationApi.submit({
        challenge_id: parseInt(id),
        user_prompt: userPrompt,
      });
      setEvaluation(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to evaluate prompt");
      console.error(err);
    } finally {
      setSubmitting(false);
    }
  };

  const getScoreColor = (score) => {
    if (score >= 8) return "text-green-600";
    if (score >= 6) return "text-yellow-600";
    return "text-red-600";
  };

  const getScoreBackground = (score) => {
    if (score >= 8) return "bg-green-50";
    if (score >= 6) return "bg-yellow-50";
    return "bg-red-50";
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  if (error && !challenge) {
    return (
      <div className="text-center py-12">
        <AlertCircle className="h-16 w-16 text-red-500 mx-auto mb-4" />
        <p className="text-red-600">{error}</p>
        <Link to="/challenges" className="btn btn-primary mt-4">
          Back to Challenges
        </Link>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <Link
          to="/challenges"
          className="inline-flex items-center text-primary-600 hover:text-primary-700 mb-4"
        >
          <ArrowLeft className="h-4 w-4 mr-2" />
          Back to Challenges
        </Link>
        <h1 className="text-3xl font-bold text-gray-900">{challenge.title}</h1>
        <p className="mt-2 text-gray-600">{challenge.description}</p>
        <div className="flex items-center gap-3 mt-4">
          <span className="badge badge-info">{challenge.category}</span>
          <span className="badge badge-warning">{challenge.difficulty}</span>
        </div>
      </div>

      {/* Challenge Details */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Goal */}
        <div className="card">
          <div className="flex items-start">
            <BookOpen className="h-6 w-6 text-primary-600 mr-3 flex-shrink-0 mt-1" />
            <div>
              <h2 className="text-lg font-semibold text-gray-900 mb-2">
                Challenge Goal
              </h2>
              <p className="text-gray-700">{challenge.goal}</p>
            </div>
          </div>
        </div>

        {/* Example Prompt */}
        <div className="card">
          <div className="flex items-start">
            <Lightbulb className="h-6 w-6 text-yellow-600 mr-3 flex-shrink-0 mt-1" />
            <div className="flex-1">
              <h2 className="text-lg font-semibold text-gray-900 mb-2">
                Example Prompt
              </h2>
              <div className="bg-gray-50 p-4 rounded-lg text-sm text-gray-700 overflow-x-auto">
                {challenge.example_prompt}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Prompt Input */}
      {!evaluation && (
        <div className="card">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">
            Your Prompt
          </h2>
          <form onSubmit={handleSubmit}>
            <textarea
              value={userPrompt}
              onChange={(e) => setUserPrompt(e.target.value)}
              placeholder="Write your prompt here... Be specific, clear, and creative!"
              rows={8}
              className="textarea mb-4"
              disabled={submitting}
            />
            {error && (
              <div className="mb-4 p-4 bg-red-50 border border-red-200 rounded-lg flex items-start">
                <AlertCircle className="h-5 w-5 text-red-600 mr-2 flex-shrink-0 mt-0.5" />
                <span className="text-sm text-red-800">{error}</span>
              </div>
            )}
            <button
              type="submit"
              disabled={submitting || !userPrompt.trim()}
              className="btn btn-primary inline-flex items-center"
            >
              {submitting ? (
                <>
                  <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                  Evaluating...
                </>
              ) : (
                <>
                  <Send className="h-4 w-4 mr-2" />
                  Submit for Evaluation
                </>
              )}
            </button>
          </form>
        </div>
      )}

      {/* Evaluation Results */}
      {evaluation && (
        <div className="space-y-6">
          {/* Overall Score */}
          <div
            className={`card ${getScoreBackground(evaluation.scores.overall)}`}
          >
            <div className="flex items-center justify-between">
              <div>
                <h2 className="text-2xl font-bold text-gray-900 mb-2">
                  Overall Score
                </h2>
                <p className="text-gray-600">
                  Great job! Here's your detailed evaluation.
                </p>
              </div>
              <div className="text-center">
                <div
                  className={`text-5xl font-bold ${getScoreColor(
                    evaluation.scores.overall
                  )}`}
                >
                  {evaluation.scores.overall.toFixed(1)}
                </div>
                <div className="text-sm text-gray-600 mt-1">out of 10</div>
              </div>
            </div>
          </div>

          {/* Score Breakdown */}
          <div className="card">
            <h2 className="text-xl font-semibold text-gray-900 mb-4 flex items-center">
              <TrendingUp className="h-5 w-5 mr-2 text-primary-600" />
              Score Breakdown
            </h2>
            <div className="grid grid-cols-2 gap-4">
              {[
                { label: "Clarity", score: evaluation.scores.clarity },
                { label: "Specificity", score: evaluation.scores.specificity },
                { label: "Creativity", score: evaluation.scores.creativity },
                { label: "Relevance", score: evaluation.scores.relevance },
              ].map((item) => (
                <div key={item.label} className="p-4 bg-gray-50 rounded-lg">
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm font-medium text-gray-700">
                      {item.label}
                    </span>
                    <span
                      className={`text-lg font-bold ${getScoreColor(
                        item.score
                      )}`}
                    >
                      {item.score.toFixed(1)}
                    </span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div
                      className={`h-2 rounded-full ${
                        item.score >= 8
                          ? "bg-green-500"
                          : item.score >= 6
                          ? "bg-yellow-500"
                          : "bg-red-500"
                      }`}
                      style={{ width: `${(item.score / 10) * 100}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Improvement Suggestions */}
          {evaluation.suggestions && evaluation.suggestions.length > 0 && (
            <div className="card">
              <h2 className="text-xl font-semibold text-gray-900 mb-4 flex items-center">
                <Sparkles className="h-5 w-5 mr-2 text-yellow-600" />
                Improvement Suggestions
              </h2>
              <div className="space-y-3">
                {evaluation.suggestions.map((suggestion, index) => (
                  <div
                    key={index}
                    className="flex items-start p-4 bg-blue-50 rounded-lg"
                  >
                    <CheckCircle className="h-5 w-5 text-blue-600 mr-3 flex-shrink-0 mt-0.5" />
                    <div>
                      <div className="flex items-center gap-2 mb-1">
                        <span className="text-sm font-medium text-blue-900 capitalize">
                          {suggestion.category}
                        </span>
                        <span
                          className={`badge ${
                            suggestion.priority === "high"
                              ? "badge-error"
                              : suggestion.priority === "medium"
                              ? "badge-warning"
                              : "badge-info"
                          }`}
                        >
                          {suggestion.priority}
                        </span>
                      </div>
                      <p className="text-sm text-gray-700">
                        {suggestion.suggestion}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* AI Output */}
          <div className="card">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">
              AI Generated Output
            </h2>
            <div className="bg-gray-50 p-4 rounded-lg">
              <p className="text-gray-700 whitespace-pre-wrap">
                {evaluation.ai_output}
              </p>
            </div>
          </div>

          {/* Actions */}
          <div className="flex gap-4">
            <button
              onClick={() => {
                setEvaluation(null);
                setUserPrompt("");
              }}
              className="btn btn-primary"
            >
              Try Again
            </button>
            <Link to="/challenges" className="btn btn-secondary">
              Next Challenge
            </Link>
          </div>
        </div>
      )}
    </div>
  );
};

export default Challenge;
