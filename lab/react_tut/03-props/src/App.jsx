import React from 'react'
import Card from './components/Card'
import diamond from '/home/satyasish/Documents/react_tut/03-props/src/assets/diamond.png'
import dounuts from '/home/satyasish/Documents/react_tut/03-props/src/assets/dounuts.png'

const App = () => {
  return (
    <div className='parent'>
        <Card user='Aman' age={26} image={dounuts} />
        <Card user="Subrata" age={62} image={diamond} />
      
    </div>
  )
}

export default App