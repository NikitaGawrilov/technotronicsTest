from battery.models import Battery
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from typing import Sequence
from fastapi import Depends
from database import get_session


class BatteryService:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def create_battery(self, name: str, paired_device_id: int | None = None) -> Battery:
        new_battery = Battery(name=name, paired_device_id=paired_device_id)
        self.session.add(new_battery)
        await self.session.commit()
        return new_battery

    async def get_all_unpaired(self) -> Sequence[Battery]:
        stmt = select(Battery).where(Battery.paired_device_id == None)
        result = await self.session.scalars(stmt)
        return result.all()

    async def get_all_paired_by_device_id(self, device_id: int) -> Sequence[Battery]:
        stmt = select(Battery).where(Battery.paired_device_id == device_id)
        result = await self.session.scalars(stmt)
        return result.all()

    async def pair_with_device(self, battery_id: int, device_id: int | None) -> Battery:
        stmt = update(Battery).where(Battery.id == battery_id).values(paired_device_id=device_id).returning(Battery)
        result = await self.session.scalar(stmt)
        await self.session.commit()
        return result

    async def rename(self, battery_id: int, name: str) -> Battery:
        stmt = update(Battery).where(Battery.id == battery_id).values(name=name).returning(Battery)
        result = await self.session.scalar(stmt)
        await self.session.commit()
        return result

    async def delete(self, battery_id: int):
        stmt = delete(Battery).where(Battery.id == battery_id).returning(Battery)
        result = await self.session.scalar(stmt)
        await self.session.commit()
        return result


async def get_battery_service(session: AsyncSession = Depends(get_session)):
    yield BatteryService(session)
