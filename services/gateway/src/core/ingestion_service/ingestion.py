
import httpx
from fastapi import UploadFile

async def forward_file(
    uploaded_file: UploadFile,
    client: httpx.AsyncClient
)-> dict:
    
    file_content = await uploaded_file.read()
    payload = {
        "uploaded_file": (
            uploaded_file.filename,
            file_content,
            uploaded_file.content_type
        )
    }

    response = await client.post(files=payload)
    return response.json()
    