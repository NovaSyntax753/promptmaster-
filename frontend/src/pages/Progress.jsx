import { useState, useEffect } from "react";
import { progressApi } from "../services/api";
import { TrendingUp, AlertTriangle, BarChart3 } from "lucide-react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const Progress = () => {
  const [trends, setTrends] = useState([]);
  const [mistakes, setMistakes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [days, setDays] = useState(30);

  useEffect(() => {
    fetchData();
  }, [days]);

  const fetchData = async () => {
    try {
      setLoading(true);
      setError(""); // Clear previous errors
      const [trendsResponse, mistakesResponse] = await Promise.all([
        progressApi.getTrends(days),
        progressApi.getMistakes(),
      ]);
      setTrends(trendsResponse.data);
      setMistakes(mistakesResponse.data);
    } catch (err) {
      console.error("Progress error:", err);
      
      let errorMessage = "Failed to load progress data";
      
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

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center py-12">
        <p className="text-red-600">{error}</p>
        <button onClick={fetchData} className="btn btn-primary mt-4">
          Retry
        </button>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-gray-900">
          Progress & Analytics
        </h1>
        <p className="mt-2 text-gray-600">Track your improvement over time</p>
      </div>

      {/* Time Range Selector */}
      <div className="card">
        <div className="flex items-center justify-between">
          <h2 className="text-lg font-semibold text-gray-900">Time Range</h2>
          <div className="flex gap-2">
            {[7, 30, 90].map((d) => (
              <button
                key={d}
                onClick={() => setDays(d)}
                className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                  days === d
                    ? "bg-primary-600 text-white"
                    : "bg-gray-100 text-gray-700 hover:bg-gray-200"
                }`}
              >
                {d} Days
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Progress Chart */}
      {trends.length > 0 ? (
        <div className="card">
          <div className="flex items-center mb-6">
            <BarChart3 className="h-6 w-6 text-primary-600 mr-2" />
            <h2 className="text-xl font-semibold text-gray-900">
              Score Trends
            </h2>
          </div>
          <ResponsiveContainer width="100%" height={400}>
            <LineChart data={trends}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis
                dataKey="date"
                tickFormatter={(date) => {
                  const d = new Date(date);
                  return `${d.getMonth() + 1}/${d.getDate()}`;
                }}
              />
              <YAxis domain={[0, 10]} />
              <Tooltip
                labelFormatter={(date) => {
                  const d = new Date(date);
                  return d.toLocaleDateString();
                }}
                formatter={(value) => [value.toFixed(1), "Score"]}
              />
              <Legend />
              <Line
                type="monotone"
                dataKey="average_score"
                stroke="#0ea5e9"
                strokeWidth={2}
                name="Average Score"
                dot={{ fill: "#0ea5e9" }}
              />
            </LineChart>
          </ResponsiveContainer>
          <div className="mt-4 text-center text-sm text-gray-600">
            Showing {trends.length} day(s) of data with{" "}
            {trends.reduce((sum, t) => sum + t.attempts, 0)} total attempts
          </div>
        </div>
      ) : (
        <div className="card text-center py-12">
          <BarChart3 className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">
            No data yet
          </h3>
          <p className="text-gray-600">
            Complete more challenges to see your progress trends
          </p>
        </div>
      )}

      {/* Top Mistakes */}
      {mistakes.length > 0 && (
        <div className="card">
          <div className="flex items-center mb-6">
            <AlertTriangle className="h-6 w-6 text-yellow-600 mr-2" />
            <h2 className="text-xl font-semibold text-gray-900">
              Areas for Improvement
            </h2>
          </div>
          <p className="text-gray-600 mb-6">
            Based on your evaluation history, here are the most common areas
            that need attention:
          </p>
          <div className="space-y-4">
            {mistakes.map((mistake, index) => (
              <div
                key={mistake.category}
                className="flex items-start p-4 bg-yellow-50 border border-yellow-200 rounded-lg"
              >
                <div className="flex-shrink-0 w-8 h-8 bg-yellow-600 text-white rounded-full flex items-center justify-center font-bold mr-4">
                  {index + 1}
                </div>
                <div className="flex-1">
                  <div className="flex items-center justify-between mb-2">
                    <h3 className="text-lg font-semibold text-gray-900 capitalize">
                      {mistake.category}
                    </h3>
                    <span className="text-sm text-gray-600">
                      {mistake.frequency} occurrence
                      {mistake.frequency !== 1 ? "s" : ""}
                    </span>
                  </div>
                  <p className="text-gray-700">{mistake.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Insights */}
      {trends.length >= 2 && (
        <div className="card bg-primary-50 border-primary-200">
          <div className="flex items-start">
            <TrendingUp className="h-6 w-6 text-primary-600 mr-3 flex-shrink-0 mt-1" />
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                💡 Insight
              </h3>
              <p className="text-gray-700">
                {(() => {
                  const recentScore = trends[trends.length - 1].average_score;
                  const oldScore = trends[0].average_score;
                  const improvement =
                    ((recentScore - oldScore) / oldScore) * 100;

                  if (improvement > 10) {
                    return `Great progress! Your scores have improved by ${improvement.toFixed(
                      1
                    )}% over the selected period. Keep up the excellent work!`;
                  } else if (improvement > 0) {
                    return `You're making steady progress with a ${improvement.toFixed(
                      1
                    )}% improvement. Consider focusing on your weaker areas to accelerate your growth.`;
                  } else if (improvement === 0) {
                    return `Your scores are stable. Try challenging yourself with harder prompts or new categories to continue improving.`;
                  } else {
                    return `Your recent scores show a ${Math.abs(
                      improvement
                    ).toFixed(
                      1
                    )}% decline. Review the feedback from your recent submissions to identify areas for improvement.`;
                  }
                })()}
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Progress;
