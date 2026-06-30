import React, {useState} from 'react'
import axios from 'axios'

const App = () => {
  
  const [file, setFile] = useState(null)
  const [response, setResponse] = useState(null)

  const handleFile = (event) => {
    const localFile = event.target.files[0]
    if (localFile)
      setFile(localFile)
  }

  const submitFile = async (event) => {
    const formdata = new FormData()
    formdata.append("file", file)
    formdata.append('upload_source', 'react_ui')

    try{
      const localResponse = await axios.post(
        // url
        'http://127.0.0.1:8000/gateway/ingest',
        // payload data
        formdata,
      )

      const data = localResponse.data
      setResponse(data)
      console.log(data);
      
    }
    catch(error) {
      if (error.response && error.response.status === 422) {
        console.error("Validation error details: ", error.response.data);
      } else {
        console.error("Upload failed", error)
      }
    }
  }
  return (
    <>
      <div className='flex flex-col gap-10 items-start'>
        <input onChange={handleFile} type='file'></input>
        <button onClick={submitFile} className='bg-black text-white'>Submit</button>
      </div>
      <div className='mt-5'>
        {response === null ? (
        <h2>Not ingested</h2>
        ):
        (
          <h2>Done with ingestion</h2>
        )
      }
      </div>
      
    </>
  )
}

export default App