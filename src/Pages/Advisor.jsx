import { useState } from 'react';

function Advisor() {
    const [query, setQuery] = useState("");
    const [response, setResponse] = useState("");

    const fetchAdvice = async () => {
        const res = await fetch(`http://127.0.0.1:8000/api/advisor/ask?query=${encodeURIComponent(query)}`);
        const data = await res.json();
        setResponse(data.response);
    };

    return (
        <div className="text-white">
            <h1 className="text-2xl font-bold mb-4">AuraFolio Advisor Chat</h1>
            <input type="text" value={query} onChange={e => setQuery(e.target.value)}
                placeholder="Ask about Rebalancing, Outlook..." className="w-full p-2 bg-gray-800 rounded mb-4"/>
            <button onClick={fetchAdvice} className="bg-green-600 px-4 py-2 rounded">Ask Advisor</button>
            {response && <div className="mt-6 bg-gray-900 p-4 rounded">{response}</div>}
        </div>
    );
}

export default Advisor;
