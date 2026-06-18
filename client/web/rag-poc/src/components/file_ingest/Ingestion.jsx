import React from 'react'
import { useState } from 'react';
import Button from './Button'
import Uploader from './Uploader'

const Ingestion = () => {
  const [isUpload, setIsUpload] = useState(false)
  const [file, setFile] = useState(null)

  const handleFileUpload = (e) => {

  }

  const isDisabled = () => {
    if (file !== null)
      setFile(true)
  }

  return (
    <div className='m-30 w-150 h-25 bg-gray-200 flex justify-between items-center'>
        <Uploader />
        <Button />
    </div>
  )
}

export default Ingestion