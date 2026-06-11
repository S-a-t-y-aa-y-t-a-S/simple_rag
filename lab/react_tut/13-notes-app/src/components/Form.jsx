import React, { useState } from 'react'

const Form = ({ addTask }) => {

  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  const handleTitle=(e) => {
    e.preventDefault()
    setTitle(e.target.value)
  }

  const handleDescription=(e)=> {
    e.preventDefault()
    setDescription(e.target.value)
    // console.log(description); for debugging
  }

  const handleLocalSubmit = (e)=> {
    e.preventDefault()
    addTask(e, title, description)
    setTitle('')
    setDescription('')
  }

  return (
    <div className='h-full ml-15 mt-15 mr-14 shrink-0 md:w-1/2 flex flex-wrap flex-col'>
      <h2 className='mb-3 font-extrabold text-3xl'>New Task</h2>
      <form onSubmit={(e)=>{handleLocalSubmit(e)}}>
        <input value={title} onChange={(e)=> {handleTitle(e)}} className='h-15 mb-5 pl-3 w-full border border-black-200 rounded-2xl' placeholder='Enter task'/>
        <textarea value={description} onChange={(e)=> {handleDescription(e)}} className='h-60 w-full mb-5 pl-3 border border-black-200 rounded-2xl' placeholder='Enter description'/>
        <button type='submit' className='px-10 py-4 bg-black text-white font-extrabold rounded-2xl active:bg-gray-400'>Submit</button>
      </form>
    </div>
  )
}

export default Form