import React from 'react'


const App = () => {
  // localStorage.setItem("age", "26") 
  // localStorage.setItem("name", "Satyasish")

  const jsonString = localStorage.getItem("user")
  const user = JSON.parse(jsonString)

  // console.log(name, age)
  console.log(jsonString);
  console.log(user)  // considered as an object

  return (
    <div>
      App
    </div>
  )
}


export default App