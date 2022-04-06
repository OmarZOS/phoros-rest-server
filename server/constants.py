
import os

QUEUES = ['Twitter','Facebook','Youtube']

EXTRACTOR_HOST = str(os.getenv("EXTRACTOR_HOST"))
EXTRACTOR_PORT = int(os.getenv("EXTRACTOR_PORT"))
EXTRACTOR_SCHEME = str(os.getenv("EXTRACTOR_SCHEME"))

STORAGE_HOST = str(os.getenv("STORAGE_HOST"))
STORAGE_PORT = int(os.getenv("STORAGE_PORT"))
STORAGE_SCHEME = str(os.getenv("STORAGE_SCHEME"))

TRANSFORMER_HOST = str(os.getenv("TRANSFORMER_HOST"))
TRANSFORMER_PORT = int(os.getenv("TRANSFORMER_PORT"))
TRANSFORMER_SCHEME = str(os.getenv("TRANSFORMER_SCHEME"))

DATA_RETRIEVAL_PATH = str(os.getenv("QUERYING_DATA_PATH"))
TRANSFORMER_SERVICE_LIST_PATH = str(os.getenv("TRANSFORMER_SERVICE_LIST_PATH"))
CENNECTIVITY_ERROR = "Error while reaching for the storage server"
