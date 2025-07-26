import { useEffect, useState } from 'react';

function HealthScore() {
    const [health, setHealth] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/portfolio/health_score')
            .then(res => res.json())
            .then(setHealth);
    }, []);

    return (
        <div className="text-white">
            <h1 className="text-2xl font-bold mb-4">Portfolio Health Score</h1>
            {health && (
                <div className="bg-gray-800 p-4 rounded">
                    <h2 className="text-3xl">Score: {health.score}%</h2>
                    <ul className="mt-2">
                        {Object.entries(health.details).map(([key, value]) => (
                            <li key={key}>{key}: {value}%</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default HealthScore;
