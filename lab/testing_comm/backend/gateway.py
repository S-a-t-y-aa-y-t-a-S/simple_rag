from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins, # allows frontend to read the data
    # allow_credentials = True,
    allow_methods = ["*"], # that is GET, POST, PUT, DELETE
    allow_headers = ["*"] # allows all headers 
)

@app.post(path='/gateway/ingest')
async def gateway_func(
    file: UploadFile = File(...),
    upload_source: str = Form(...),
):
    file_contents = await file.read()

    # reconstruct the files payload for the next service
    files = {
        # this is the actual file content
        'file': (
            file.filename, 
            file_contents,
            file.content_type
        )
    }
    
    data = { # this is the metadata
        'upload_source': upload_source
    } 

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url="http://127.0.0.1:8001/ingestion/ingest",
            follow_redirects=True,
            timeout=10,
            data=data,
            files=files
        )

        return response.json()

    