import React from 'react'
import Card from './components/Card'
import Navbar from './components/Navbar'

const App = () => {
  const name = "Satyasish"
  const age = 26

  return (
    <div>
      <div className='card-beta'>
        <h1>Hello i am {name}</h1>
        <h2>I am {age} years old</h2>
      </div>
      <div className='card-beta'><Card /></div>
      <div className='card-beta'><Card /></div>
      <div className='card-beta'><Navbar /></div>
    </div>
  )
}

export default App