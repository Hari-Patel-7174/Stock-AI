import { useEffect, useState } from 'react';
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from 'recharts';

function Portfolio() {
    const [allocation, setAllocation] = useState([]);
    const [holdings, setHoldings] = useState([]);
    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/portfolio/allocation')
            .then(res => res.json())
            .then(setAllocation);

        fetch('http://127.0.0.1:8000/api/portfolio/holdings')
            .then(res => res.json())
            .then(setHoldings);

        fetch('http://127.0.0.1:8000/api/portfolio/rebalance_alerts')
            .then(res => res.json())
            .then(setAlerts);
    }, []);

    const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8'];

    return (
        <div className="text-white">
            <h1 className="text-2xl font-bold mb-4">Portfolio Analysis</h1>

            <div className="grid grid-cols-2 gap-6">
                {/* Donut Chart */}
                <div className="bg-gray-800 p-4 rounded-lg">
                    <h2 className="text-xl mb-2">Asset Allocation</h2>
                    <ResponsiveContainer width="100%" height={300}>
                        <PieChart>
                            <Pie
                                data={allocation}
                                dataKey="percent"
                                nameKey="sector"
                                cx="50%"
                                cy="50%"
                                innerRadius={70}
                                outerRadius={100}
                                fill="#8884d8"
                                label
                            >
                                {allocation.map((entry, index) => (
                                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                                ))}
                            </Pie>
                            <Tooltip />
                        </PieChart>
                    </ResponsiveContainer>
                </div>

                {/* Holdings Table */}
                <div className="bg-gray-800 p-4 rounded-lg">
                    <h2 className="text-xl mb-2">Your Holdings</h2>
                    <table className="w-full text-left">
                        <thead>
                            <tr>
                                <th>Ticker</th>
                                <th>Quantity</th>
                                <th>Avg. Price</th>
                                <th>Current Value</th>
                                <th>P/L</th>
                            </tr>
                        </thead>
                        <tbody>
                            {holdings.map(stock => (
                                <tr key={stock.ticker}>
                                    <td>{stock.ticker}</td>
                                    <td>{stock.quantity}</td>
                                    <td>₹{stock.avg_price}</td>
                                    <td>₹{stock.current_value}</td>
                                    <td className={stock.pl_percent >= 0 ? "text-green-400" : "text-red-400"}>
                                        {stock.pl_percent}%
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>

            {/* Rebalancing Alerts */}
            <div className="bg-gray-900 mt-6 p-4 rounded-lg">
                <h2 className="text-xl mb-2">Rebalancing Suggestions</h2>
                {alerts.length === 0 ? <p>No Rebalancing Needed</p> :
                    alerts.map((alert, idx) => (
                        <p key={idx} className="text-yellow-400">{alert}</p>
                    ))
                }
            </div>
        </div>
    );
}

export default Portfolio;
