import { useEffect } from 'react'
import React, { useState } from 'react'


const App = () => {

  const [a, setA] = useState(0)
  const [b, setB] = useState(0)

  const changingA = () => {
    console.log('A is chaging');
  }

  const changingB = () => {
    console.log('B is changing');
  }

  useEffect(function display() {
    changingA()
    console.log('use effect is used')
  }, [a])

  useEffect(function display() {
    changingB()
    console.log('use effect is used')
  }, [b]) // here b is the dependency

  return (
    <div>
      <h3 className='ml-4'>a = {a}</h3>
      <h3 className='ml-4'>b = {b}</h3>
      <button className='px-8 py-4 m-3 bg-black text-white ' onClick={()=>{setA(a+1)}}>Change A</button>
      <button className='px-8 py-4 m-3 bg-black text-white' onClick={()=>{setB(b-1)}}>Change B</button>
    </div>
  )
}

export default App