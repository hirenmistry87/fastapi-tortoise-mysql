from pydantic import BaseModel

class ReadBase(BaseModel):
    model_config = {"from_attributes": True}