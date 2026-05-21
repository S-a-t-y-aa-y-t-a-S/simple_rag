
import httpx
from dependencies.schema_validator import URLConfig, ServiceCommConfig
from utils.constants import DefaultVals


url_config = URLConfig()
service_comm_config = ServiceCommConfig()


async def get_ingestion_client()-> httpx.AsyncClient:
    return httpx.AsyncClient(
        base_url=f"{url_config.host}:{url_config.port}",
        follow_redirects=DefaultVals.DEFAULT_BOOL_VALUE,
        timeout=service_comm_config.timeout
    )