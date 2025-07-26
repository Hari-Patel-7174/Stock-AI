import { useState } from 'react';

function Login({ setUser }) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        const res = await fetch('http://127.0.0.1:8000/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        const data = await res.json();
        if (res.ok) {
            setUser({ email, watchlist: data.watchlist });
        } else {
            alert(data.detail);
        }
    };

    return (
        <div className="text-white p-6">
            <h1 className="text-2xl mb-4">Login</h1>
            <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} className="w-full mb-2 p-2 bg-gray-700 rounded"/>
            <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} className="w-full mb-4 p-2 bg-gray-700 rounded"/>
            <button onClick={handleLogin} className="bg-blue-600 px-4 py-2 rounded">Login</button>
        </div>
    );
}

export default Login;
