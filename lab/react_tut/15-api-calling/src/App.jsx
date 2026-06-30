import React from 'react'
import axios from 'axios'
import { useState } from 'react'

const App = () => {

  const [data, setData] = useState([])

  // using ordinary fetch()
  // const handleClick = async () => {
  //   const response = await fetch('https://jsonplaceholder.typicode.com/todos')
  //   const response_json_data = await response.json()
  //   console.log(response);
  //   console.log(response_json_data)
  // }

  // using axios
  const handleClick = async () => {
    const response = await axios.get('https://picsum.photos/v2/list')
    const response_data = await response.data
    console.log(response_data);
    
    setData([...response_data]) 
    console.log(data)
  }

  

  return (
    <div>
      <button onClick={handleClick} className='m-10 px-10 py-5 rounded-xl bg-black text-white active:bg-gray-400'>Click me!</button>
      <div>
        {
        data.length === 0 ? (
          <p className='ml-10'>Nothing to display</p>
        ):
        (
          data.map((val, idx)=>(
            <h3 key={idx} className='text-black text-wrap px-10'>Hello {val.author} {idx+1}</h3>
          ))
        )
      }
      </div>
      
    
    </div>
  )
}

export default App