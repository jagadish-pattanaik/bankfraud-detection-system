import {
  FileText,
  AlertTriangle,
  CheckCircle,
} from "lucide-react";

const SummaryCards = ({ result }) => {

  if (!result) return null;

  const cards = [
    {
      title: "Total Records",
      value: result.total_records,
      icon: <FileText className="w-8 h-8 text-blue-600" />,
      color: "border-blue-500",
    },
    {
      title: "Fraud Accounts",
      value: result.fraud_accounts,
      icon: <AlertTriangle className="w-8 h-8 text-red-500" />,
      color: "border-red-500",
    },
    {
      title: "Legitimate Accounts",
      value: result.legitimate_accounts,
      icon: <CheckCircle className="w-8 h-8 text-green-500" />,
      color: "border-green-500",
    },
  ];

  return (
    <div className="grid md:grid-cols-3 gap-6 mt-10">

      {cards.map((card) => (
        <div
          key={card.title}
          className={`bg-white rounded-xl shadow-md p-6 border-l-4 ${card.color}`}
        >

          <div className="flex justify-between items-center">
            <div>
              <p className="text-gray-500">
                {card.title}
              </p>

              <h2 className="text-3xl font-bold mt-2">
                {card.value}
              </h2>
            </div>

            {card.icon}
          </div>

        </div>
      ))}

    </div>
  );
};

export default SummaryCards;