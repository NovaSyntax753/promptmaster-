import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { progressApi } from "../services/api";
import { Target, TrendingUp, Award, BookOpen, ArrowRight } from "lucide-react";

const Dashboard = () => {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      setLoading(true);
      console.log("Fetching dashboard data...");
      const response = await progressApi.getDashboard();
      console.log("Dashboard response:", response.data);
      setStats(response.data);
    } catch (err) {
      console.error("Dashboard error details:", err);
      console.error("Error response:", err.response?.data);
      console.error("Error status:", err.response?.status);
      setError(
        `Failed to load dashboard data: ${
          err.response?.data?.detail || err.message
        }`
      );
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
        <button onClick={fetchDashboard} className="btn btn-primary mt-4">
          Retry
        </button>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <p className="mt-2 text-gray-600">
          Track your prompt engineering progress
        </p>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <div className="card">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <Target className="h-8 w-8 text-primary-600" />
            </div>
            <div className="ml-4">
              <p className="text-sm font-medium text-gray-500">
                Total Attempts
              </p>
              <p className="text-2xl font-bold text-gray-900">
                {stats?.total_attempts || 0}
              </p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <Award className="h-8 w-8 text-yellow-600" />
            </div>
            <div className="ml-4">
              <p className="text-sm font-medium text-gray-500">Average Score</p>
              <p className="text-2xl font-bold text-gray-900">
                {stats?.average_score?.toFixed(1) || "0.0"}/10
              </p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <TrendingUp
                className={`h-8 w-8 ${
                  (stats?.improvement_rate || 0) >= 0
                    ? "text-green-600"
                    : "text-red-600"
                }`}
              />
            </div>
            <div className="ml-4">
              <p className="text-sm font-medium text-gray-500">Improvement</p>
              <p
                className={`text-2xl font-bold ${
                  (stats?.improvement_rate || 0) >= 0
                    ? "text-green-600"
                    : "text-red-600"
                }`}
              >
                {stats?.improvement_rate >= 0 ? "+" : ""}
                {stats?.improvement_rate?.toFixed(1) || "0.0"}%
              </p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <BookOpen className="h-8 w-8 text-blue-600" />
            </div>
            <div className="ml-4">
              <p className="text-sm font-medium text-gray-500">Best Category</p>
              <p className="text-lg font-bold text-gray-900">
                {stats?.best_category || "None"}
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="card">
        <h2 className="text-xl font-bold text-gray-900 mb-4">Quick Actions</h2>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
          <Link
            to="/challenges"
            className="flex items-center justify-between p-4 bg-primary-50 rounded-lg hover:bg-primary-100 transition-colors"
          >
            <div className="flex items-center">
              <BookOpen className="h-6 w-6 text-primary-600 mr-3" />
              <span className="font-medium text-gray-900">
                Browse Challenges
              </span>
            </div>
            <ArrowRight className="h-5 w-5 text-primary-600" />
          </Link>

          <Link
            to="/progress"
            className="flex items-center justify-between p-4 bg-green-50 rounded-lg hover:bg-green-100 transition-colors"
          >
            <div className="flex items-center">
              <TrendingUp className="h-6 w-6 text-green-600 mr-3" />
              <span className="font-medium text-gray-900">View Progress</span>
            </div>
            <ArrowRight className="h-5 w-5 text-green-600" />
          </Link>
        </div>
      </div>

      {/* Category Performance */}
      {stats?.attempts_by_category &&
        Object.keys(stats.attempts_by_category).length > 0 && (
          <div className="card">
            <h2 className="text-xl font-bold text-gray-900 mb-4">
              Category Performance
            </h2>
            <div className="space-y-4">
              {Object.entries(stats.attempts_by_category).map(
                ([category, count]) => (
                  <div key={category}>
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-sm font-medium text-gray-700">
                        {category}
                      </span>
                      <span className="text-sm text-gray-500">
                        {count} attempts
                      </span>
                    </div>
                    <div className="w-full bg-gray-200 rounded-full h-2">
                      <div
                        className="bg-primary-600 h-2 rounded-full"
                        style={{
                          width: `${(count / stats.total_attempts) * 100}%`,
                        }}
                      />
                    </div>
                  </div>
                )
              )}
            </div>
          </div>
        )}

      {/* Empty State */}
      {stats?.total_attempts === 0 && (
        <div className="card text-center py-12">
          <Target className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">
            No attempts yet
          </h3>
          <p className="text-gray-600 mb-6">
            Start your journey by trying your first challenge!
          </p>
          <Link
            to="/challenges"
            className="btn btn-primary inline-flex items-center"
          >
            <BookOpen className="h-5 w-5 mr-2" />
            Browse Challenges
          </Link>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
