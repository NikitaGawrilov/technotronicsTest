from fastapi import APIRouter, Depends
from battery.services import BatteryService, get_battery_service
from battery.schemas import *
from typing import Sequence
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError


battery_router = APIRouter(
    prefix='/battery',
    tags=['Battery']
)


@battery_router.get('/unpaired', response_model=Sequence[BatteryResponse])
async def get_unpaired(service: BatteryService = Depends(get_battery_service)):
    return await service.get_all_unpaired()


@battery_router.get('/paired', response_model=Sequence[BatteryResponse])
async def get_paired(device_id: int, service: BatteryService = Depends(get_battery_service)):
    return await service.get_all_paired_by_device_id(device_id=device_id)


@battery_router.post('/create', response_model=BatteryResponse)
async def create_battery(battery: BatteryCreateRequest, service: BatteryService = Depends(get_battery_service)):
    try:
        result = await service.create_battery(name=battery.name, paired_device_id=battery.paired_device_id)
    except IntegrityError:
        raise HTTPException(400, 'Указанного устройства не существует!')
    return result


@battery_router.put('/rename', response_model=BatteryResponse)
async def rename_battery(
        battery: BatteryRenameRequest = Depends(BatteryRenameRequest),
        service: BatteryService = Depends(get_battery_service)
):
    return await service.rename(
        battery_id=battery.battery_id,
        name=battery.name
    )


@battery_router.put('/pair', response_model=BatteryResponse)
async def pair_battery(
        battery_id: int,
        device_id: int | None = None,
        service: BatteryService = Depends(get_battery_service)
):
    try:
        result = await service.pair_with_device(
            battery_id=battery_id,
            device_id=device_id
        )
        if result is None:
            raise HTTPException(400, 'Указанного аккумулятора не существует!')
    except IntegrityError:
        raise HTTPException(400, 'Указанного устройства не существует!')
    return result


@battery_router.delete('/delete', response_model=BatteryResponse)
async def delete_battery(
    battery: BatteryDeleteRequest = Depends(BatteryDeleteRequest),
    service: BatteryService = Depends(get_battery_service)
):
    return await service.delete(battery_id=battery.battery_id)
