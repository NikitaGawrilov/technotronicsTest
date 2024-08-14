from pydantic import BaseModel
from datetime import datetime


# Схемы для валидации запросов и ответов
class DeviceCreateRequest(BaseModel):
    name: str


class DeviceRenameRequest(BaseModel):
    device_id: int
    name: str


class DeviceDeleteRequest(BaseModel):
    device_id: int


class DeviceResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
