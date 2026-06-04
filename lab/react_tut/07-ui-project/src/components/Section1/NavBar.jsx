import React from 'react'

const NavBar = () => {
  return (
    <div className='flex justify-between'>
        <div className='text-white bg-black text-sm rounded-full px-10 py-4 mt-5 ml-5 uppercase tracking-wider'>Target Audience</div>
        <div className='text-black bg-gray-200 text-sm rounded-full px-10 py-4 mt-5 mr-5 uppercase tracking-wider'>Digital banking platform</div>
    </div>
  )
}

export default NavBar