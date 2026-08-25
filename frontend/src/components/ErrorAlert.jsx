import { TriangleAlert } from "lucide-react";

const ErrorAlert = ({ message }) => {
  if (!message) return null;

  return (
    <div className="max-w-3xl mx-auto mt-6">
      <div className="flex items-center gap-3 rounded-lg border border-red-300 bg-red-50 p-4">
        <TriangleAlert className="w-6 h-6 text-red-600" />

        <p className="text-red-700 font-medium">
          {message}
        </p>
      </div>
    </div>
  );
};

export default ErrorAlert;