import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import Dashboard from './components/Dashboard';
import Water3D from './components/Water3D';
import ChatPanel from './components/ChatPanel';

const theme = createTheme({
  palette: {
    primary: { main: '#2c3e50' },
    secondary: { main: '#3498db' }
  }
});

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <Router>
        <Routes>
          <Route path="/" element={
            <div className="dashboard-container">
              <Water3D />
              <Dashboard />
              <ChatPanel />
            </div>
          }/>
        </Routes>
      </Router>
    </ThemeProvider>
  );
}