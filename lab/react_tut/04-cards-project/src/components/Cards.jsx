import React from 'react'
import {Bookmark} from 'lucide-react'

const Cards = (props) => {
  return (
    
      <div className="card">
        
        <div className="top">
            <img src={props.logo}></img>
            <button>Save <Bookmark size={12}/></button>
        </div>
        <div className="center">
          <h3>{props.name}<span>{props.published} days ago</span></h3>
          <h2>{props.designation} Designer</h2>  
            <div className = 'parent-h4'>
              <h4>{props.time}</h4>
              <h4>{props.level}</h4>
            </div>        
        </div>
        
        <div className="bottom">
          <div className='position'>
            <h3>{props.payment}</h3>
            <p>{props.place}, India</p>
          </div>
          <button>Apply now</button>
        </div>
      </div>  
  )
}

export default Cards