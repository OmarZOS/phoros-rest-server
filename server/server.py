
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

# ----------- Storage ----------------------------------------

@app.get("/storage")
def storage():
    return {"message": "Hello World"}

@app.post("/storage/query")
def storage_submit_query(query: Query):
    return {"message": "Hello World"}

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

