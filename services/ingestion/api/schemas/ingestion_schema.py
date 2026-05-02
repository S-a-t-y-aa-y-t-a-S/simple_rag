from pydantic import BaseModel

class IngestionResponse(BaseModel):
    return_statement: str