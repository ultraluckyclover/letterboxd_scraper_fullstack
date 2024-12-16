import React, { useState } from 'react'

export const InputUser = ( { onLogin } ) => {

    const [user, setUser] = useState("")

    const handleSubmit = (e) => {
      e.preventDefault();
      console.log("entered:" , {user})
      onLogin(user)
    }



  return (
    <div>
        <h2>Input username</h2>
        <form onSubmit = {handleSubmit}>
            <input 
            type = 'text' 
            placeholder = 'Input username'
            value = {user}
            onChange = {e => setUser(e.target.value)} />
            <button type = 'submit'> Submit </button>
        </form>

    </div>
  )
}
