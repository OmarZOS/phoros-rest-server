
import json
from constants import *
import httpx

# accessing reverse proxy services..
url_transformer_proxy = f"{TRANSFORMER_SCHEME}://{TRANSFORMER_HOST}:{TRANSFORMER_PORT}"

service_list_path= TRANSFORMER_SERVICE_LIST_PATH

async def get_services(args):
    
    res = await httpx.get(url_transformer_proxy+service_list_path)
    
    # TODO: test this..
    return res.content.decode()



    
    