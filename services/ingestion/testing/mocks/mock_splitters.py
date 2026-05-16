
from src.microservices.loader_n_splitter.splitters import Splitter
from src.dependencies.helpers import Helper
from .. import constants

splitter = Splitter(
    helper=Helper()
)
print(splitter.doc_splitter(documents=constants.SAMPLE_DOCUMENT))