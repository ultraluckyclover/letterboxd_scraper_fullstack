import React, { useState } from 'react'

export const InputUser = () => {

    const [input, setInput] = useState("")
  return (
    <div>
        <h2>Input username</h2>
        <form>
            <input 
            type = 'text' 
            placeholder = 'Input username'
            value = {input}
            onChange = {e => setInput(e.target.value)} />
            <button type = 'submit'> Submit </button>
        </form>

    </div>
  )
}
