import { Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import AgentDetail from './pages/AgentDetail'
import Navbar from './components/Navbar'

function App() {
  return (
    <div className="app">
      <Navbar />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/agent/:id" element={<AgentDetail />} />
        </Routes>
      </main>
    </div>
  )
}

export default App
