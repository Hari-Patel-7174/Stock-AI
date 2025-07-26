import { useEffect, useState } from 'react';
import { getHighSentimentStocks } from '../../services/scannerAPI';
import ScannerCard from '../../components/ScannerCard';

function Dashboard() {
    const [highSentiment, setHighSentiment] = useState([]);

    useEffect(() => {
        getHighSentimentStocks().then(data => setHighSentiment(data));
    }, []);

    return (
        <div>
            <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
            <div className="grid grid-cols-3 gap-4">
                {highSentiment.map(stock => (
                    <ScannerCard key={stock.ticker} stock={stock} />
                ))}
            </div>
        </div>
    );
}

export default Dashboard;
