import { LoaderCircle } from "lucide-react";

const LoadingSpinner = () => {
  return (
    <div className="flex flex-col items-center justify-center py-10">
      <LoaderCircle className="w-12 h-12 text-blue-600 animate-spin" />

      <p className="mt-4 text-gray-600 font-medium">
        Uploading file and predicting fraud...
      </p>
    </div>
  );
};

export default LoadingSpinner;