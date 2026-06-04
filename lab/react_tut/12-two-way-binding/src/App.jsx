import React, { useState } from 'react'
import './App.css'

const App = () => {

  const [title, setTitle] = useState("")
  const submitHandler = (e) => {
    e.preventDefault()
    console.log(title)
    setTitle("")
    // console.log("file is not found");
    
  }

  return (
    <div>
      <form onSubmit={(e) =>{
        submitHandler(e)
      }}>
      <input onChange={(e)=> {
        setTitle(e.target.value)
        console.log(e.target.value)
      }}/>
      <button type="submit">Submit</button>
    </form>
    </div>
  )
}

export default App