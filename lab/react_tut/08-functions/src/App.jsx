import React from 'react'
import './App.css'



// const App = () => {

//   const onBtnClick = () => {
//     console.log('button is clicked')
//   }

//   function mouseEnter() {
//     console.log('mouse entered')
//   }

//   return (
//     <div>
//       <button onClick={onBtnClick}>Click here</button>
//       <button onClick={mouseEnter}>mouse</button>
//     </div>
//   )
// }

// onClick
// onDoubleClick
// 

const App = () => {

  const btnCick = () => {
    console.log('button is clicked')
  }

  return (
    <div>
      <button onClick={btnClick}>Click</button>
    </div>

  )
}

export default App