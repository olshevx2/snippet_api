from pydantic import BaseModel

class SnippetCreate(BaseModel):
    title: str
    code: str

class SnippetResponse(BaseModel):
    uuid: str
    title: str
    code: str
    class Config:
        from_attributes = True