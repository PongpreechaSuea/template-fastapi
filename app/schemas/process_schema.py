from typing import Union

from pydantic import BaseModel


class TextContent(BaseModel):
    type: str = 'text' 
    text: str

class ImageContent(BaseModel):
    type: str = 'image' 
    image_url: str 

IContent = Union[TextContent, ImageContent]