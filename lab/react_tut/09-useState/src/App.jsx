import React from 'react'
import {useState} from 'react'
import './App.css'

const App = () => {

  const [num, setNum] = useState(0);

  const increaseNum = () => {
    setNum(num+1)
    console.log('Value of num = ', num+1);
  }

  const decreaseNum = () => {
    setNum(num-1)
    console.log("Value of num = ", num-1)
  }

  const increaseBy5 = () => {
    setNum(num+5)
    console.log("Value of num = ", num+5)
  }

  return (
    <div>
      <h1>{num}</h1>
      <button onClick={increaseNum}>increase</button>
      <button onClick={decreaseNum}>decrease</button>
      <div>
        <button className='btn' onClick={increaseBy5}>Increase by 5</button>
      </div>
    </div>
  )
}

export default App