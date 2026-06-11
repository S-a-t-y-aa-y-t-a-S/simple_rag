import React, { useState, useEffect } from 'react'
import Form from './components/Form.jsx'
import RecentTasks from './components/RecentTasks.jsx'

const App = () => {

  let [tasks, setTasks] = useState([])

  useEffect(()=>{
    console.log(tasks);
  }, [tasks])

  const handleSubmit = (e, title, description)=> {
    // e.preventDefault()
    setTasks(tasks=> [...tasks, {title, description}])
  }

  const handleDeletion = (taskID)=> {
    const copyTasks = [...tasks]
    copyTasks.splice(taskID, 1) 
    setTasks(copyTasks)
  }

  return (
    <div className='h-full w-screen'>
      <div className='pb-5 h-screen overflow-y-hidden flex'>
        <Form addTask={handleSubmit} /> {/* using the setter function here to be called in child*/}
      <div className='md:w-1/2 lg:border-l-2 lg:border-l-gray-300 pl-13 mt-15'>
        <h2 className='font-extrabold text-3xl'>Recent Tasks</h2>
          {
          tasks.length === 0 ? (
            <h1 className='flex flex-col mt-100 place-items-center text-gray-500 font-sans'>Please enter a note</h1>
          ):
          (
            <div className='mt-2 h-full overflow-y-auto content-start flex flex-wrap'>
              {
                tasks.map((task, index)=> (
                <RecentTasks 
                key = {index} // not included into the object
                id = {index}
                title = {task.title}
                description = {task.description}
                deleteTask = {handleDeletion}
              />))
              }
            </div>   
          )
        }
        </div>
      </div>
      </div>
      
    
  )
}

export default App