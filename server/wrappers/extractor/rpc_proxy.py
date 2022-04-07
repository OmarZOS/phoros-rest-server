from constants import *
import xmlrpc.client

# the extractor instances are rpc servers

global proxy_extractor 
proxy_extractor=None

def get_session():
    global proxy_extractor
    if(not proxy_extractor):
        url_proxy_extractor="{}://{}:{}".format(EXTRACTOR_SCHEME,EXTRACTOR_HOST,EXTRACTOR_PORT)
        proxy_extractor = xmlrpc.client.ServerProxy(url_proxy_extractor)
    
    return proxy_extractor
    
def list_workers():
    return get_session().list_workers()

def submit_job(job):
    print(job.model)
    return get_session().start_harvesting_data(job.api_name,job.model,job.starting_node)

def get(var):
    return get_session().get(var)

def set(var,val):
    return get_session().set(var,val)
    
def get_all():
    return get_session().get_all_vars()

def get_schemas():
    return get_session().show_schemas()
