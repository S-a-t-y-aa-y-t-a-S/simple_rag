import React from 'react'
import RightCards from './RightCards'
import pic1 from '/home/satyasish/Documents/react_tut/07-ui-project/src/assets/christina-wocintechchat-com-m-0Zx1bDv5BNY-unsplash.jpg'
import pic2 from '/home/satyasish/Documents/react_tut/07-ui-project/src/assets/pic2.png'
import pic3 from '/home/satyasish/Documents/react_tut/07-ui-project/src/assets/pic3.png'

const RightContent = () => {

  const items = [
    {
      background_img: pic1,
      description: 'Prime customers, that have access to bank credit and are satisfied with the current product',
      tag: 'Satisfied'
    },
    {
      background_img: pic2,
      description: 'Prime customers, that have access to bank credit and are not satisfied with the current product',
      tag: 'Underserved'
    },
    {
      background_img: pic3,
      description: 'Customers from near prime and sub-prime segments with no access to bank credit',
      tag: 'Underbanked'
    },
    {
      background_img: pic1,
      description: 'Prime customers, that have access to bank credit and are satisfied with the current product',
      tag: 'Satisfied'
    },
  ];

  return (
    <div id = "right" className='relative h-full w-3/4 flex gap-5 overflow-x-auto'>
    {
      items.map((item, idx) => (
        <RightCards 
          id={idx+1}
          background_img={item.background_img}
          description={item.description}
          tag={item.tag}
        />
    ))}
    
    </div>
  )
}

export default RightContent