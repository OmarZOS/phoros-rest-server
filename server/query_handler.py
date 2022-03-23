
import wrappers.transformer.transformer as url_transformer_proxy
# import wrappers.extractor.rpc_proxy as extractor_proxy 
import wrappers.storage.storage as storage_service

# --------------------- Extraction -----------------------------

def list_workers():
    res  = extractor_proxy.list_workers()
    return {"message": f"Hallo von {res}."}

def submit_job(job):
    res = extractor_proxy.submit_job(job)
    return {"message": f"Es ist getan!! {res}."}

async def fetch_data(api,content,roadmap):
    return await storage_service.get_data(api,content,roadmap)

async def get_transformation_services(args):
    pass