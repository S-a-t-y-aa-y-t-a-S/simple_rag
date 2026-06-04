import React from 'react'


const Card = (props) => {
    console.log(props.user)
    console.log(props.age)
    return (
        <div>
            <div className='card'>
                <img src={props.image} alt='image'></img>
                <h1>Satyasish Patranabish</h1>
                <h3>name: {props.user}</h3>
                <h3>age: {props.age}</h3>
                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit.</p>
                <button>View profile</button>
            </div>
        </div>
    )
}

export default Card