import React from 'react'

const Button = ({isDisabled, handleIngestion}) => {

  const buttonActive = () => {
    if ({isDisabled} === true)
        console.log('button is disabled');
    else {
      console.log("button is enabled")
      handleIngestion()
    }
  }
  
  return (
    <div>
        <button
        type='button' 
        onClick={buttonActive}
        disabled={isDisabled} 
        className='
        h-15 mr-8 mx-2 px-3 py-0.5 bg-black text-white font-bold rounded-2xl active:scale-90
        disabled:cursor-not-allowed disabled:scale-100 disabled:bg-gray-600' >Ingest File</button>
    </div>
  )
}

export default Button
