from pydantic import BaseModel
from typing import Optional


# ---------- Data models: ---------------------------------------

class Transformation(BaseModel):
    name: str
    url: str
    description: Optional[str] = None
    # tax: Optional[float] = None

class Extraction(BaseModel):
    api_name: str
    model: Optional[dict] = None
    starting_node: Optional[dict] = None

class Query(BaseModel):
    content: dict
    roadmap: Optional[str] = None