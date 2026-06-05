import React from 'react'

const Form = () => {
  return (
    <div className='h-full w-1/2 ml-15 mt-15 shrink-0 md:w-1/2 flex flex-wrap flex-col'>
      <h2 className='mb-3 font-extrabold text-3xl'>New Task</h2>
      <form>
        <input className='h-15 mb-5 pl-3 w-full border border-black-200 rounded-2xl' placeholder='Enter task'/>
        <textarea className='h-60 w-full mb-5 pl-3 border border-black-200 rounded-2xl' placeholder='Enter description'/>
        <button className='px-10 py-4 bg-black text-white font-extrabold rounded-2xl'>Submit</button>
      </form>
    </div>
  )
}

export default Form