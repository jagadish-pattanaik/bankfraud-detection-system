import { UploadCloud } from "lucide-react";

const UploadBox = ({
  selectedFile,
  setSelectedFile,
  onUpload,
  loading,
}) => {
  const handleFileChange = (e) => {
    if (e.target.files.length > 0) {
      setSelectedFile(e.target.files[0]);
    }
  };

  return (
    <div className="max-w-3xl mx-auto bg-white rounded-xl shadow-lg p-8">

      <label className="border-2 border-dashed border-blue-400 rounded-xl p-10 flex flex-col items-center justify-center cursor-pointer hover:bg-blue-50 transition">

        <UploadCloud className="w-14 h-14 text-blue-600" />

        <h2 className="mt-4 text-xl font-semibold">
          Drag & Drop CSV/XLSX File
        </h2>

        <p className="text-gray-500 mt-2">
          or click to browse
        </p>

        <input
          type="file"
          accept=".csv,.xlsx"
          className="hidden"
          onChange={handleFileChange}
        />
      </label>

      {selectedFile && (
        <div className="mt-5 bg-gray-100 rounded-lg p-3">
          <p className="font-medium">
            Selected File:
          </p>

          <p className="text-blue-600">
            {selectedFile.name}
          </p>
        </div>
      )}

      <button
        disabled={!selectedFile || loading}
        onClick={onUpload}
        className="w-full mt-6 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg disabled:bg-gray-400"
      >
        {loading ? "Predicting..." : "Predict Fraud"}
      </button>

    </div>
  );
};

export default UploadBox;