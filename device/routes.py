from fastapi import APIRouter, Depends
from device.services import DeviceService, get_device_service
from device.schemas import *
from typing import Sequence


device_router = APIRouter(
    prefix='/device',
    tags=['Device']
)


@device_router.get('/all', response_model=Sequence[DeviceResponse])
async def get_all(service: DeviceService = Depends(get_device_service)):
    return await service.get_all()


@device_router.post('/create', response_model=DeviceResponse)
async def create_device(device: DeviceCreateRequest, service: DeviceService = Depends(get_device_service)):
    return await service.create_device(name=device.name)


@device_router.put('/rename', response_model=DeviceResponse)
async def rename_device(
        device: DeviceRenameRequest = Depends(DeviceRenameRequest),
        service: DeviceService = Depends(get_device_service)
):
    return await service.rename(
        device_id=device.device_id,
        name=device.name
    )


@device_router.delete('/delete', response_model=DeviceResponse)
async def delete_device(
    device: DeviceDeleteRequest = Depends(DeviceDeleteRequest),
    service: DeviceService = Depends(get_device_service)
):
    return await service.delete(device_id=device.device_id)
