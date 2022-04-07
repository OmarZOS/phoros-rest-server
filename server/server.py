
from fastapi import FastAPI

from models import *
from constants import *
import query_handler as handler

# ----------- App initialisation ---------------------------------------

app = FastAPI();

extractor_services = {}

@app.get("/")
def root():
    return {"message": "Welcome to phoros' services"}

# ----------- Extraction -------------------------------------

@app.get("/extractors")
def extractors():
    return {"message": "Hello in the extraction services. you can access /submit to add a new extractor"}

@app.post("/extractors/test")
def extractors_list_worker():
    return handler.list_workers()

@app.post("/extractors/submit")
def extractor_submit_job(job : Extraction):
    return handler.submit_job(job)

@app.post("/extractors/getvalue")
def extractor_get_val(varname:str):
    return handler.get_value(varname)

@app.post("/extractors/setvalue")
def extractor_set_val(varname:str,val:str):
    return handler.set_value(varname,val)

@app.get("/extractors/getall")
def extractor_get_all():
    return handler.get_all()

@app.get("/extractors/get_schemas")
def extractor_get_schemas():
    return handler.get_schemas()

# ----------- Storage ----------------------------------------

@app.get("/storage")
def storage():
    return {"message": "Hello World"}

@app.post("/storage/query")
def storage_query(query: Query):
    return handler.fetch_data(query.api,query.content,query.roadmap)

# ----------- Transformation ---------------------------------

@app.get("/transformers")
def transformers():
    return {"message": "Hello World"}

@app.post("/transformers/add")
def transformers_add(transformer: Transformation):
    return {"message": "Hello World"}

@app.post("/transformers/delete")
def transformers_delete():
    return {"message": "Hello World"}

