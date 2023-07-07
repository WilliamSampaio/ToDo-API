from typing import Optional

from pydantic import BaseModel

from data import StatusOption


class ItemModel(BaseModel):
    titulo: str
    descricao: Optional[str]
    status: Optional[StatusOption]


class ItemResponseModel(ItemModel):
    id: int
