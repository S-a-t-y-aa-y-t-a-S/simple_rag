
import httpx
from dependencies.yaml_extractor import YamlExtractor
from utils.constants import DefaultVals


class ServiceClients:

    def __init__(self):
        self.__extactor: YamlExtractor = YamlExtractor()
        self.__url_config = self.__extactor.get_url_config()
        self.__service_comm_config = self.__extactor.get_service_comm_config()

    async def get_ingestion_client(self)-> httpx.AsyncClient:
        return httpx.AsyncClient(
            base_url=f"{self.__url_config.host}:{self.__url_config.port}",
            follow_redirects=DefaultVals.DEFAULT_BOOL_VALUE,
            timeout=self.__service_comm_config.timeout
        )