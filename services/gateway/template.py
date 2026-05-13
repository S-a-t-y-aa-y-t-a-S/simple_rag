from pydantic import BaseModel, Field
from fastapi import FastAPI, UploadFile, status, HTTPException, File
import tempfile, os, httpx

# app = FastAPI()

# class IngestionSchema(BaseModel):
#     uploaded_file_path: str 


# INGESTION_URL = "http://127.0.0.1:8001/ingest"


# @app.post(path="/ingest")
# def forward_to_ingestion(payload: IngestionSchema):
#     data = payload.uploaded_file_path
#     with httpx.Client() as client:
#         try:
#             # Must match the POST operation defined in your FastAPI ingestion service
#             response = client.post(INGESTION_URL, 
#                 params={"file_path": data},
#                 timeout=60.0
#             )
            
#             # Checks for HTTP errors (like 405 Method Not Allowed or 422 Validation Error)
#             response.raise_for_status()
            
#             # This captures the successful string/JSON response from FastAPI
#             return response.json() 
            

#         except httpx.HTTPStatusError as exp:
#             raise HTTPException(status_code=exp.response.status_code, detail=exp.response.text)

#         except httpx.HTTPStatusError as exp:
#             raise HTTPException(status_code=504, detail=f"Ingestion service unreachable: {exp}")    

from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException
import httpx

app = FastAPI(redirect_slashes=False)

# 1. Define a Pydantic model for the incoming Postman JSON body
class IngestRequest(BaseModel):
    payload_data: str

INGESTION_URL = "http://127.0.0.1:8001"

# 2. Use the Pydantic model as the type hint
@app.post(path="/ingest")
def forward_to_ingestion(request_body: IngestRequest):
    # Extract the string from the model
    file_path_value = request_body.payload_data
    
    with httpx.Client() as client:
        try:
            # 3. Match the Ingestion service's parameter name ("file_path")
            # We pass it as a query parameter using the 'params' argument
            # because 'def ingest_doc(file_path: str)' expects a query string
            response = client.post(
                INGESTION_URL, 
                params={"file_path": file_path_value},
                timeout=60.0 # Embeddings can take time; increase the timeout
            )
            
            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
        except httpx.RequestError as e:
            raise HTTPException(status_code=504, detail=f"Ingestion service unreachable: {e}")
