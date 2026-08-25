import { ShieldCheck } from "lucide-react";

const Navbar = () => {
  return (
    <nav className="bg-white shadow-sm border-b">
      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center">
        <div className="flex items-center gap-3">
          <div className="bg-blue-600 p-2 rounded-lg">
            <ShieldCheck className="text-white w-6 h-6" />
          </div>

          <div>
            <h1 className="text-xl font-bold text-gray-800">
              Bank Fraud Detection
            </h1>
            <p className="text-sm text-gray-500">
              AI Powered Fraud Detection System
            </p>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;