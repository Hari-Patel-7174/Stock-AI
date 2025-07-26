import { useEffect, useState } from 'react';

function Watchlist({ user }) {
    const [watchlist, setWatchlist] = useState(user.watchlist);
    const [newTicker, setNewTicker] = useState("");

    const addTicker = async () => {
        const res = await fetch('http://127.0.0.1:8000/api/watchlist/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: user.email, ticker: newTicker })
        });
        const data = await res.json();
        setWatchlist(data.watchlist);
        setNewTicker("");
    };

    return (
        <div className="text-white">
            <h1 className="text-2xl font-bold mb-4">Your Watchlist</h1>
            <ul className="mb-4">
                {watchlist.map((ticker, idx) => (
                    <li key={idx} className="mb-2 bg-gray-800 p-2 rounded">{ticker}</li>
                ))}
            </ul>
            <input type="text" placeholder="Add Ticker" value={newTicker} onChange={e => setNewTicker(e.target.value)} className="p-2 bg-gray-700 rounded mr-2"/>
            <button onClick={addTicker} className="bg-green-600 px-4 py-2 rounded">Add</button>
        </div>
    );
}

export default Watchlist;
