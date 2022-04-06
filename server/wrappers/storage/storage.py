
# the REST service of the social storage component
import json
from constants import *
import asyncio
import httpx

url_storage_server = f"{STORAGE_SCHEME}://{STORAGE_HOST}:{STORAGE_PORT}"
data_retrieval_path = DATA_RETRIEVAL_PATH

async def get_data(api,content,roadmap):
    
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    try:
        # res = requests.get(url_storage_server)
        print(url_storage_server+data_retrieval_path)
        res = await httpx.post(url_storage_server+data_retrieval_path
                                ,headers=headers
                                ,data=json.dumps({
                                    "api":api
                                        ,"content":content
                                        ,"roadmap":roadmap
                                })
                            )
        return json.loads(res.content.decode())["_resp"]['data']
    except Exception as r:
        return CENNECTIVITY_ERROR + str(r) 



