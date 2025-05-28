from typing import List

from beanie import Document, PydanticObjectId
from schemas import IContent


class FileDocument(Document):
    class Settings:
        name = "files"
        arbitrary_types_allowed = True

    name: str
    originURL: str
    content: List[IContent]
    token: int
    userId: PydanticObjectId
    aiId: PydanticObjectId