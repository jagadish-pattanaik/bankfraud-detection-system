const Footer = () => {
  return (
    <footer className="mt-16 border-t bg-white">
      <div className="max-w-7xl mx-auto px-6 py-6 text-center">

        <h2 className="font-semibold text-gray-800">
          Bank Fraud Detection System
        </h2>

        <p className="text-gray-500 mt-2">
          Built with FastAPI • React • Tailwind CSS • XGBoost
        </p>

        <p className="text-sm text-gray-400 mt-4">
          © {new Date().getFullYear()} All Rights Reserved
        </p>

      </div>
    </footer>
  );
};

export default Footer;