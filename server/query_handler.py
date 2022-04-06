import wrappers.transformer.transformer as url_transformer_proxy
import wrappers.extractor.rpc_proxy as extractor_proxy 
import wrappers.storage.storage as storage_service

# --------------------- Extraction -----------------------------

def list_workers():
    res  = extractor_proxy.list_workers()
    return {"message": f"Hallo von {res}."}

def submit_job(job):
    res = extractor_proxy.submit_job(job)
    return {"message": f"Es ist getan!! {res}."}

def get_value(var):
    return extractor_proxy.get(var)

def get_all():
    return extractor_proxy.get_all()

def set_value(var,val):
    return extractor_proxy.set(var,val)

def fetch_data(api,content,roadmap):
    return storage_service.get_data(api,content,roadmap)

def get_transformation_services(args):
    pass