import React from 'react'
import { ArrowRight } from 'lucide-react'

const RightCards = (props) => {
  return (
    <div className='h-full w-100 shrink-0 overflow-hidden relative rounded-4xl'>
      <img src={props.background_img} className='h-full w-full object-cover' />
      <div className='absolute top-0 left-0 h-full w-full p-10 flex flex-col'>
        <h3 className='h-20 w-10 mb-80 font-bold text-2xl rounded-full flex justify-center items-center bg-white'>{props.id}</h3>
        <div className='h-full flex flex-col justify-between'>
          <p className='text-white mb-40 pr-10 text-xl'>{props.description}</p>
        <div className='h-15 flex justify-between'>
          <button className='pl-5 w-55 bg-blue-300 rounded-2xl font-bold text-white text-left'>{props.tag}</button>
          <div className='h-15 w-15 mr-3 p-4 rounded-full bg-blue-600'>
            <ArrowRight size={32} color='white'/>
          </div>
        </div>
      </div>
    </div>
        </div>
        
  )
}

export default RightCards