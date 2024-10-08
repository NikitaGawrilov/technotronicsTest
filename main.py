from fastapi import FastAPI
from device.routes import device_router
from battery.routes import battery_router

# Инициализация приложения
app = FastAPI(
    title='Technotronics Test Case by N. Gavrilov'
)

# Подключение роутеров
app.include_router(device_router)
app.include_router(battery_router)
