import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Scanners from './pages/Scanners';
import Portfolio from './pages/Portfolio';

const API_URL = import.meta.env.VITE_API_URL;


function App() {
    return (
        <Router>
            <div className="flex">
                <Sidebar />
                <div className="flex-grow p-6">
                    <Routes>
                        <Route path="/" element={<Dashboard />} />
                        <Route path="/scanners" element={<Scanners />} />
                        <Route path="/portfolio" element={<Portfolio />} />
                    </Routes>
                </div>
            </div>
        </Router>
    );
}

export default App;
