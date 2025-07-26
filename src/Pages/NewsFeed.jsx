import { useEffect, useState } from 'react';

function NewsFeed() {
    const [news, setNews] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/newsfeed/latest?ticker=RELIANCE')
            .then(res => res.json())
            .then(setNews);
    }, []);

    return (
        <div className="text-white">
            <h1 className="text-2xl font-bold mb-4">Live News Feed</h1>
            <ul>
                {news.map((item, idx) => (
                    <li key={idx} className="mb-2">
                        <a href={item.url} target="_blank" className="text-blue-400 underline">{item.title}</a>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default NewsFeed;
