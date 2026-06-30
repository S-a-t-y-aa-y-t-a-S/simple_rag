import React from 'react'

const Uploader = ({handleFileUpload}) => {
  return (
    <div className='w-100 p-5 ml-5 rounded-2xl  bg-gray-300 text-nowrap flex justify-center'>
        <label for='upload' className='cursor-pointer'>
          upload a file
          <input onChange={handleFileUpload} type="file" id='upload' className='hidden' />
        </label>
    </div>
  )
}

export default Uploader