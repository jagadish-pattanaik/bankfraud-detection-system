import { useState } from "react";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import UploadBox from "../components/UploadBox";
import SummaryCards from "../components/SummaryCards";
import LoadingSpinner from "../components/LoadingSpinner";
import ErrorAlert from "../components/ErrorAlert";
import Footer from "../components/Footer";

import { uploadFile } from "../services/api";

const Home = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!selectedFile) {
      setError("Please select a CSV or XLSX file.");
      return;
    }

    try {
      setLoading(true);
      setError("");
      setResult(null);

      const response = await uploadFile(selectedFile);
      console.log("Backend Response:", response);

      setResult(response);
    } catch (err) {
      setError(
        err.response?.data?.detail ||
          "Something went wrong. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-100">
      <Navbar />

      <Hero />

      <div className="max-w-5xl mx-auto px-4">

        <UploadBox
          selectedFile={selectedFile}
          setSelectedFile={setSelectedFile}
          onUpload={handleUpload}
          loading={loading}
        />

        {loading && <LoadingSpinner />}

        <ErrorAlert message={error} />

        <SummaryCards result={result} />

        {result && (
          <div className="text-center mt-8">
            <a
              href={result.download_url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-lg font-semibold"
            >
              Download Prediction CSV
            </a>
          </div>
        )}
      </div>

      <Footer />
    </div>
  );
};

export default Home;