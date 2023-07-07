from typing import Optional
from pydantic import BaseModel


class ItemModel(BaseModel):
    titulo: str
    descricao: Optional[str]
    status: Optional[str]
