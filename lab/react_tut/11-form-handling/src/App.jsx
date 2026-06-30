import React from 'react'
import { useState } from 'react'
import './App.css'

const App = () => {
  
  const [name, setName] = useState("")
  const [displayName, setDisplayName] = useState("")

  const displayEnteredName = (e) => {
    e.preventDefault()
    // setDisplayName(name) // updating once on submitting the form, where this function gets triggered
    // console.log(name); 
    console.log("form is submitted");
      
  }

  return (
    <div>
      <form onSubmit={displayEnteredName}>
        <input type='text' value={name} onChange={(e)=>{
          setName(e.target.value) // updating every a character is typed
        }} placeholder='Enter your name'></input>
        <button>Submit</button>
      </form>
    </div>
  )
}

export default App