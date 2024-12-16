import { useState, useEffect } from 'react'
import './App.css';
import Movie from './components/Movie/Movie'
import { Home } from './components/Home/Home';
import { InputUser } from './components/InputUser/InputUser';
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  const [username, setUsername] = useState(null);

  const handleLogin = (username) => {
    setUsername(username);
  };

  // return (<div className = 'App'>
  //   { username ? ( <Home username = {username}/> ) : (<InputUser onLogin = {handleLogin}/> ) }
  // </div>)

  if (!username){
    return <InputUser onLogin = {handleLogin} />;
  }

  return ( 
    <>
      <BrowserRouter> 
        <Routes>
          <Route path = '/' element = { <Home /> } /> 
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App;
