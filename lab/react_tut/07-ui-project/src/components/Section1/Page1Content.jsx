import React from 'react'
import LeftContent from './LeftContent'
import RightContent from './RightContent'
 
const Page1Content = () => {
  // bg-emerald-500
  return (
    <div className='py-10 px-5 flex items-center gap-10 h-[90vh] '>
      <LeftContent />
      <RightContent />
    </div>
  )
}

export default Page1Content