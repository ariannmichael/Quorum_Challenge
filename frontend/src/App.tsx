import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import ThemeProvider from 'react-bootstrap/ThemeProvider';
import Home from './components/pages/home/Home';
import Header from "./components/commons/Header";
import Legislators from "./components/pages/legislators/Legislators";
import Bills from "./components/pages/bills/Bills";

function App() {
  return (
    <ThemeProvider>
      <Header />
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/legislators" element={<Legislators />} />
                <Route path="/bills" element={<Bills />} />
                <Route path="*" element={<Navigate to="/" replace />} />
            </Routes>
        </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;
