import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { evaluationApi } from "../services/api";
import {
  History as HistoryIcon,
  Calendar,
  Target,
  ExternalLink,
} from "lucide-react";

const History = () => {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [page, setPage] = useState(0);
  const [hasMore, setHasMore] = useState(true);

  useEffect(() => {
    fetchHistory();
  }, [page]);

  const fetchHistory = async () => {
    try {
      setLoading(true);
      setError(""); // Clear previous errors
      const response = await evaluationApi.getHistory({
        limit: 10,
        offset: page * 10,
      });

      if (page === 0) {
        setHistory(response.data);
      } else {
        setHistory([...history, ...response.data]);
      }

      setHasMore(response.data.length === 10);
    } catch (err) {
      console.error("History error:", err);
      
      let errorMessage = "Failed to load history";
      
      if (err.code === 'ECONNABORTED' || err.message.includes('timeout')) {
        errorMessage = "Server is waking up (free tier). This may take up to 60 seconds. Please wait and try again.";
      } else if (err.message === 'Network Error' || !err.response) {
        errorMessage = "Cannot connect to server. The backend might be starting up (this takes 30-60 seconds on free tier). Please wait and retry.";
      }
      
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const getScoreColor = (score) => {
    if (score >= 8) return "text-green-600 bg-green-50";
    if (score >= 6) return "text-yellow-600 bg-yellow-50";
    return "text-red-600 bg-red-50";
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    }).format(date);
  };

  if (loading && page === 0) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Evaluation History</h1>
        <p className="mt-2 text-gray-600">
          Review your past prompt submissions and scores
        </p>
      </div>

      {/* History List */}
      {error ? (
        <div className="text-center py-12">
          <p className="text-red-600">{error}</p>
          <button
            onClick={() => fetchHistory()}
            className="btn btn-primary mt-4"
          >
            Retry
          </button>
        </div>
      ) : history.length === 0 ? (
        <div className="card text-center py-12">
          <HistoryIcon className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">
            No history yet
          </h3>
          <p className="text-gray-600 mb-6">
            Start completing challenges to see your evaluation history here
          </p>
          <Link
            to="/challenges"
            className="btn btn-primary inline-flex items-center"
          >
            <Target className="h-5 w-5 mr-2" />
            Browse Challenges
          </Link>
        </div>
      ) : (
        <>
          <div className="space-y-4">
            {history.map((evaluation) => (
              <div
                key={evaluation.id}
                className="card hover:shadow-md transition-shadow"
              >
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <h3 className="text-lg font-semibold text-gray-900">
                        Challenge #{evaluation.challenge_id}
                      </h3>
                      <span
                        className={`px-3 py-1 rounded-full text-sm font-bold ${getScoreColor(
                          evaluation.scores.overall
                        )}`}
                      >
                        {evaluation.scores.overall.toFixed(1)}/10
                      </span>
                    </div>

                    <div className="flex items-center text-sm text-gray-500 mb-3">
                      <Calendar className="h-4 w-4 mr-1" />
                      {formatDate(evaluation.created_at)}
                    </div>

                    <div className="bg-gray-50 p-3 rounded-lg mb-3">
                      <p className="text-sm text-gray-700 line-clamp-2">
                        {evaluation.user_prompt}
                      </p>
                    </div>

                    <div className="grid grid-cols-4 gap-3 text-sm">
                      <div>
                        <span className="text-gray-500">Clarity</span>
                        <div className="font-semibold text-gray-900">
                          {evaluation.scores.clarity.toFixed(1)}
                        </div>
                      </div>
                      <div>
                        <span className="text-gray-500">Specificity</span>
                        <div className="font-semibold text-gray-900">
                          {evaluation.scores.specificity.toFixed(1)}
                        </div>
                      </div>
                      <div>
                        <span className="text-gray-500">Creativity</span>
                        <div className="font-semibold text-gray-900">
                          {evaluation.scores.creativity.toFixed(1)}
                        </div>
                      </div>
                      <div>
                        <span className="text-gray-500">Relevance</span>
                        <div className="font-semibold text-gray-900">
                          {evaluation.scores.relevance.toFixed(1)}
                        </div>
                      </div>
                    </div>

                    {evaluation.suggestions &&
                      evaluation.suggestions.length > 0 && (
                        <div className="mt-3 pt-3 border-t border-gray-200">
                          <p className="text-sm text-gray-600 mb-2">
                            <strong>{evaluation.suggestions.length}</strong>{" "}
                            improvement suggestions
                          </p>
                        </div>
                      )}
                  </div>

                  <Link
                    to={`/challenges/${evaluation.challenge_id}`}
                    className="ml-4 btn btn-secondary inline-flex items-center"
                  >
                    <ExternalLink className="h-4 w-4 mr-2" />
                    Retry
                  </Link>
                </div>
              </div>
            ))}
          </div>

          {/* Load More */}
          {hasMore && (
            <div className="text-center">
              <button
                onClick={() => setPage(page + 1)}
                disabled={loading}
                className="btn btn-secondary"
              >
                {loading ? "Loading..." : "Load More"}
              </button>
            </div>
          )}
        </>
      )}
    </div>
  );
};

export default History;
