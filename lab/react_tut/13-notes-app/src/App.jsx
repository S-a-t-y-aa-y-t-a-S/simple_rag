import React from 'react'
import Form from './components/Form.jsx'
import RecentTasks from './components/RecentTasks.jsx'
// import Form from './components/form_layout/Form.jsx'
// import DisplayNotes from './components/display_notes/DisplayNotes.jsx'

const App = () => {
  return (
    <div className='overflow-hidden h-screen w-screen flex'>
      <Form />
      <RecentTasks />
    </div>
    
  )
}

export default App