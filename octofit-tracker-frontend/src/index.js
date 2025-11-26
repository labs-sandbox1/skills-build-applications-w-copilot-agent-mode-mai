
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Optionally set REACT_APP_CODESPACE_NAME from window if available
if (window && window.location && window.location.hostname) {
  const match = window.location.hostname.match(/^(.*)-8000\.app\.github\.dev$/);
  if (match && match[1]) {
    process.env.REACT_APP_CODESPACE_NAME = match[1];
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
