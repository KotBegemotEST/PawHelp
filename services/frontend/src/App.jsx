import React from 'react'
import Header from './components/Header.jsx'
import Footer from './components/Footer.jsx'
import LoginPage from './pages/LoginPage.jsx'
import DashboardPage from './pages/DashboardPage.jsx'


import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import HomePage from "./pages/HomePage";

function App() {
  // const [count, setCount] = useState(0)

  return (
    <Router>
      <Header />
      <Routes>
        {/* <Route path="/" element={<HomePage />} /> */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/dashboard" element={<DashboardPage/>}/>
        {/* <Route path="/map" element={<MapPage/>}/> */}

      </Routes>
      <Footer />
    </Router>

  )
}

export default App
