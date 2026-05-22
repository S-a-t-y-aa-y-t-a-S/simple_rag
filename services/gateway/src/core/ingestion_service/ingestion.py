
import httpx
from fastapi import UploadFile
from dependencies.schema_validator import URLConfig
from dependencies.yaml_extractor import YamlExtractor

url_config = YamlExtractor().get_url_config()


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

    response = await client.post(
        url=url_config.endpoint,
        files=payload)
    
    return response
    