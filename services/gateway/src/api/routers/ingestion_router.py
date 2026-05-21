
from fastapi import APIRouter, UploadFile, Depends
import httpx
from core.ingestion_service.ingestion import get