import React from 'react'
import { X } from 'lucide-react'

const RecentTasks = (props) => {

    return (
            <div className='h-100 w-80 bg-black text-white rounded-3xl shadow-xl mb-8 mr-8'>
                    <div className='ml-70 mt-4'>
                    <X onClick={()=>(props.deleteTask(props.id))} className='cursor-pointer' />
                    </div>
                    <div className='flex flex-col items-center ml-1 mt-10 gap-10'>
                        <h2 className='mb-3 text-2xl text-wrap font-bold'>{props.title}</h2>
                        <p className='h-55 overflow-y-scroll ml-3 text-wrap text-gray-200 text-medium'>{props.description}</p>
                    </div>
                </div>  
            
    )
}


export default RecentTasks
// Lorem ipsum, dolor sit amet consectetur adipisicing elit. Inventore officia ipsam accusamus illum officiis ex eligendi cupiditate expedita, quos obcaecati quisquam commodi veritatis quasi consectetur nisi dolore quas impedit distinctio?