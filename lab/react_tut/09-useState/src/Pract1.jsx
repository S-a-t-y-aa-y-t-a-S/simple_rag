import React, {useState} from 'react'

const Pract1 = () => {

    // const [num, setNum] = useState({user: 'Rishi', age: 17})
    const [num, setNum] = useState(10)
    const btnClicked = () => {
        // // **batch update**
        console.log(num+3)
        setNum(prev => (prev+1))
        setNum(prev => (prev+1))
        setNum(prev => (prev+1))
    }



    // const btnClicked = () => {

    //     setNum(prev=> ({...prev, age:50})) // immediately return an object
        
        // const newNum = [...num]
        // newNum.push(99)
        // console.log(newNum)



        // const newNum = {...num}
        // newNum.user = "Aman"
        // newNum.age = 26
        
        // console.log("updated name: ", newNum.user)
        // console.log("updated age: ", newNum.age)

    //     setNum(newNum)
    // }

    return (
    <div>
        <h1>{num}</h1>
        <button onClick={btnClicked}>Click</button>
    </div>
)
}

export default Pract1