
from ingestion.main_scripts.loader_n_splitter.splitters import Splitter
from ingestion.utils.helper import Helper
from .. import constants

splitter = Splitter(
    helper=Helper()
)
print(splitter.doc_splitter(documents=constants.SAMPLE_DOCUMENT))