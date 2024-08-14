from device.models import Device
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from typing import Sequence
from fastapi import Depends
from database import get_session


# Класс-сервис (DAL) для устройств
class DeviceService:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    # create
    async def create_device(self, name: str) -> Device:
        new_device = Device(name=name)
        self.session.add(new_device)
        await self.session.commit()
        return new_device

    # read
    async def get_all(self) -> Sequence[Device]:
        stmt = select(Device)
        result = await self.session.scalars(stmt)
        return result.all()

    # update
    async def rename(self, device_id: int, name: str) -> Device:
        stmt = update(Device).where(Device.id == device_id).values(name=name).returning(Device)
        result = await self.session.scalar(stmt)
        await self.session.commit()
        return result

    # delete
    async def delete(self, device_id: int):
        stmt = delete(Device).where(Device.id == device_id).returning(Device)
        result = await self.session.scalar(stmt)
        await self.session.commit()
        return result


# функция-генератор объекта сервисного класса
async def get_device_service(session: AsyncSession = Depends(get_session)):
    yield DeviceService(session)
