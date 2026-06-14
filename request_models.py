from pydantic import BaseModel, HttpUrl

class URLCheckRequest(BaseModel):
    url: str  # Using str to allow flexibility in handling input before parsing