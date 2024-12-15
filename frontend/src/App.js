import { useState, useEffect } from 'react'
import './App.css';
import Movie from './components/Movie/Movie'
import { Home } from './components/Home/Home';
import { InputUser } from './components/InputUser/InputUser';

function App() {
  const [username, setUsername] = useState(null);

  const handleLogin = (username) => {
    setUsername(username);
  };

  return (<div className = 'App'>
    { username ? ( <Home username = {username}/> ) : (<InputUser onLogin = {handleLogin}/> ) }
  </div>)
}

export default App;
