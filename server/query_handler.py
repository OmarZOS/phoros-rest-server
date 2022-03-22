
import wrappers.extractor.rpc_proxy as extractor_proxy 
import wrappers.storage.storage as storage_service
import wrappers.transformer.transformer as url_transformer_proxy

# --------------------- Extraction -----------------------------

def list_workers():
    res  = extractor_proxy.list_workers()
    return {"message": f"Hallo von {res}."}

def submit_job(job):
    res = extractor_proxy.submit_job(job)
    return {"message": f"Es ist getan!! {res}."}


