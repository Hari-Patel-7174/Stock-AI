import { useState } from 'react';

function Insights() {
    const [newsInput, setNewsInput] = useState("");
    const [insight, setInsight] = useState("");

    const fetchInsight = async () => {
        const response = await fetch(`http://127.0.0.1:8000/api/insights/summary?news=${encodeURIComponent(newsInput)}`);
        const data = await response.json();
        setInsight(data.insight);
    };

    return (
        <div className="text-white">
            <h1 className="text-2xl font-bold mb-4">AI Stock Insight Generator</h1>
            <textarea value={newsInput} onChange={e => setNewsInput(e.target.value)}
                placeholder="Paste News Headline or Paragraph..." className="w-full h-32 p-2 bg-gray-800 rounded mb-4"/>
            <button onClick={fetchInsight} className="bg-blue-600 px-4 py-2 rounded">Generate Insight</button>
            {insight && <div className="mt-6 bg-gray-900 p-4 rounded">{insight}</div>}
        </div>
    );
}

export default Insights;
