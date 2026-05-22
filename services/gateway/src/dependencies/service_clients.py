
import httpx
from dependencies.yaml_extractor import YamlExtractor
from utils.constants import DefaultVals


extactor = YamlExtractor()
url_config = extactor.get_url_config()
service_comm_config = extactor.get_service_comm_config()


async def get_ingestion_client()-> httpx.AsyncClient:
    return httpx.AsyncClient(
        base_url=f"{url_config.host}:{url_config.port}",
        follow_redirects=DefaultVals.DEFAULT_BOOL_VALUE,
        timeout=service_comm_config.timeout
    )