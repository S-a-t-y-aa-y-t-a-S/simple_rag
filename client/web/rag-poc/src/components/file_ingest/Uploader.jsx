import React from 'react'

const Uploader = () => {
  return (
    <div className='w-100 p-5 ml-5 rounded-2xl  bg-gray-300 text-nowrap flex justify-center'>
        <input type="file" id='upload' className='hidden'></input>
        <label for='upload' className='cursor-pointer'>upload a file</label>
    </div>
  )
}

export default Uploader