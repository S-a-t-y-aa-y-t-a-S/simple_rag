
from fastapi import FastAPI, UploadFile
import httpx

from pydantic import BaseModel, Field
from fastapi import UploadFile, File



app = FastAPI()

INGESTION_URL = "http://127.0.0.1:8001/ingest"

# 2. Use the Pydantic model as the type hint
@app.post(path="/ingest")
async def forward_to_ingestion(uploaded_file: UploadFile):
    file_content = await uploaded_file.read()
            
    payload = {
        "uploaded_file": (uploaded_file.filename, file_content, uploaded_file.content_type)
    }


    async with httpx.AsyncClient(follow_redirects=True) as client:
    
        response = await client.post(
            INGESTION_URL,
            files=payload,
            timeout=10
        )
        
        # response.raise_for_status()
        return response.json() 

       