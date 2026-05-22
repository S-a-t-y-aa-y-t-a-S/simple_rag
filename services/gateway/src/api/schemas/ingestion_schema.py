
from pydantic import BaseModel

class IngestResponse(BaseModel):
    status: int
    message: str
    content: dict
    