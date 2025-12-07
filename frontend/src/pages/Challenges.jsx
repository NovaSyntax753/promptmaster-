import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { challengesApi } from "../services/api";
import { BookOpen, Code, FileText, Database, ChevronRight } from "lucide-react";

const Challenges = () => {
  const [challenges, setChallenges] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("all");
  const [selectedDifficulty, setSelectedDifficulty] = useState("all");

  const categories = [
    { value: "all", label: "All Categories", icon: BookOpen },
    { value: "Creative Writing", label: "Creative Writing", icon: FileText },
    { value: "Coding & Debugging", label: "Coding & Debugging", icon: Code },
    {
      value: "Summarization & Rewriting",
      label: "Summarization",
      icon: FileText,
    },
    { value: "Data Extraction", label: "Data Extraction", icon: Database },
  ];

  const difficulties = [
    { value: "all", label: "All Levels" },
    { value: "beginner", label: "Beginner" },
    { value: "intermediate", label: "Intermediate" },
    { value: "advanced", label: "Advanced" },
  ];

  useEffect(() => {
    fetchChallenges();
  }, [selectedCategory, selectedDifficulty]);

  const fetchChallenges = async () => {
    try {
      setLoading(true);
      setError("");
      const params = {};
      if (selectedCategory !== "all") params.category = selectedCategory;
      if (selectedDifficulty !== "all")
        params.difficulty = selectedDifficulty.toLowerCase();

      console.log("Fetching challenges with params:", params);
      const response = await challengesApi.getAll(params);
      console.log("Challenges API response:", response);
      console.log("Challenges data:", response.data);

      // Handle both response.data (array) and direct array response
      const challengesData = Array.isArray(response.data)
        ? response.data
        : response.data?.data || [];
      setChallenges(challengesData);

      if (challengesData.length === 0) {
        console.warn("No challenges returned from API");
      }
    } catch (err) {
      console.error("Challenges error:", err);

      let errorMessage = "Failed to load challenges";

      if (err.code === "ECONNABORTED" || err.message.includes("timeout")) {
        errorMessage =
          "Server is waking up (free tier). This may take up to 60 seconds. Please wait and try again.";
      } else if (err.message === "Network Error" || !err.response) {
        errorMessage =
          "Cannot connect to server. The backend might be starting up (this takes 30-60 seconds on free tier). Please wait and retry.";
      } else if (err.response?.data?.detail) {
        errorMessage = err.response.data.detail;
      }

      setError(errorMessage);
      console.error("Error response:", err.response);
    } finally {
      setLoading(false);
    }
  };

  const getDifficultyColor = (difficulty) => {
    const colors = {
      beginner: "bg-green-100 text-green-800",
      intermediate: "bg-yellow-100 text-yellow-800",
      advanced: "bg-red-100 text-red-800",
    };
    return colors[difficulty] || "bg-gray-100 text-gray-800";
  };

  const getCategoryIcon = (category) => {
    const icons = {
      "Creative Writing": FileText,
      "Coding & Debugging": Code,
      "Summarization & Rewriting": FileText,
      "Data Extraction": Database,
    };
    return icons[category] || BookOpen;
  };

  if (loading) {
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
        <h1 className="text-3xl font-bold text-gray-900">Challenges</h1>
        <p className="mt-2 text-gray-600">
          Choose a challenge to test your prompt engineering skills
        </p>
      </div>

      {/* Filters */}
      <div className="card">
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Category
            </label>
            <select
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
              className="input"
            >
              {categories.map((cat) => (
                <option key={cat.value} value={cat.value}>
                  {cat.label}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Difficulty
            </label>
            <select
              value={selectedDifficulty}
              onChange={(e) => setSelectedDifficulty(e.target.value)}
              className="input"
            >
              {difficulties.map((diff) => (
                <option key={diff.value} value={diff.value}>
                  {diff.label}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {/* Challenges Grid */}
      {error ? (
        <div className="text-center py-12">
          <p className="text-red-600">{error}</p>
          <button onClick={fetchChallenges} className="btn btn-primary mt-4">
            Retry
          </button>
        </div>
      ) : challenges.length === 0 ? (
        <div className="card text-center py-12">
          <BookOpen className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">
            No challenges found
          </h3>
          <p className="text-gray-600">Try adjusting your filters</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          {challenges.map((challenge) => {
            const Icon = getCategoryIcon(challenge.category);
            return (
              <Link
                key={challenge.id}
                to={`/challenges/${challenge.id}`}
                className="card hover:shadow-md transition-shadow group"
              >
                <div className="flex items-start justify-between mb-4">
                  <div className="flex items-center">
                    <div className="p-2 bg-primary-50 rounded-lg">
                      <Icon className="h-6 w-6 text-primary-600" />
                    </div>
                  </div>
                  <span
                    className={`badge ${getDifficultyColor(
                      challenge.difficulty
                    )}`}
                  >
                    {challenge.difficulty}
                  </span>
                </div>

                <h3 className="text-lg font-semibold text-gray-900 mb-2 group-hover:text-primary-600 transition-colors">
                  {challenge.title}
                </h3>

                <p className="text-sm text-gray-600 mb-4 line-clamp-2">
                  {challenge.description}
                </p>

                <div className="flex items-center justify-between pt-4 border-t border-gray-200">
                  <span className="text-xs text-gray-500">
                    {challenge.category}
                  </span>
                  <ChevronRight className="h-5 w-5 text-gray-400 group-hover:text-primary-600 transition-colors" />
                </div>
              </Link>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default Challenges;
