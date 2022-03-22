from constants import *
import xmlrpc.client

# the extractor instances are rpc servers
url_proxy_extractor="{}://{}:{}".format(EXTRACTOR_SCHEME,EXTRACTOR_HOST,EXTRACTOR_PORT)
proxy_extractor = xmlrpc.client.ServerProxy(url_proxy_extractor)

def list_workers():
    return proxy_extractor.list_workers()

def submit_job(job):
    return proxy_extractor.start_harvesting_data(job.api_name,job.model,job.starting_node)