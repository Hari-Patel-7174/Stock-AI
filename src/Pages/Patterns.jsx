import { useEffect, useState } from 'react';

function Patterns() {
    const [breakouts, setBreakouts] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/patterns/breakouts')
            .then(res => res.json())
            .then(setBreakouts);
    }, []);

    return (
        <div className="text-white">
            <h1 className="text-2xl font-bold mb-4">Pattern Breakouts</h1>
            <div className="grid grid-cols-2 gap-4">
                {breakouts.map((item, idx) => (
                    <div key={idx} className="bg-gray-800 p-4 rounded">
                        <h3 className="text-xl">{item.ticker}</h3>
                        <p>Pattern: {item.pattern}</p>
                        <p>Breakout Price: ₹{item.price}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Patterns;
