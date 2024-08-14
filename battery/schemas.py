from pydantic import BaseModel
from datetime import datetime


# Схемы для валидации запросов и ответов
class BatteryCreateRequest(BaseModel):
    name: str
    paired_device_id: int | None = None


class BatteryRenameRequest(BaseModel):
    battery_id: int
    name: str


class BatteryDeleteRequest(BaseModel):
    battery_id: int


class BatteryGetPairedRequest(BaseModel):
    device_id: int


class BatteryResponse(BaseModel):
    id: int
    name: str
    paired_device_id: int | None
    created_at: datetime
