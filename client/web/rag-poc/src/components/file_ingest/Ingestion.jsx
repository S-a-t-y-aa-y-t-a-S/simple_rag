import React from 'react'
import { useState } from 'react';
import Button from './Button'
import Uploader from './Uploader'
import Playground from './Playground';
import axios from 'axios';


const Ingestion = () => {
  const [file, setFile] = useState(null)
  const [flag, setFlag] = useState(0)

  const handleFileUpload = (event) => {
    const uploadedFile = event.target.files[0]
    console.log(uploadedFile);
    
    if(uploadedFile) {
      setFile(uploadedFile)
      setFlag(flag+1)
      alert('File has been uploaded. Press the ingestion button to proceed..')
      console.log("flag = ", flag)
    }
  }

  const handleIngestion = async () => {
    setFlag(flag+1)
    console.log("flag = ", flag)
    const formData = new FormData()
    formData.append("uploaded_file", file)

    const localResponse = await axios.post("http://localhost:8000/ingest", formData)
    const input_data = localResponse.data
    if (input_data) {
      setFlag(flag+2)
      console.log("flag = ", flag)
    }
  }

  const isDisabled = !file
 
  return (
    <>
      <div className='m-30 w-150 h-25 bg-gray-200 flex justify-between items-center'>
        <Uploader handleFileUpload={handleFileUpload} />
        <Button isDisabled={isDisabled} handleIngestion={handleIngestion} />
      </div>
      <Playground flag={flag} />     
    </>
  )
}

export default Ingestion