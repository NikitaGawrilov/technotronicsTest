from fastapi import FastAPI
from services.device import DeviceService
from fastapi import Depends
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(
    title='Technotronics Test Case by N. Gavrilov'
)


@app.delete('/')
async def hello(device_id: int, session: AsyncSession = Depends(get_session)):
    s = DeviceService(session)
    return await s.delete(device_id=device_id)
