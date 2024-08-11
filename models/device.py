from sqlalchemy import Integer, VARCHAR, TIMESTAMP, Column
from datetime import datetime as dt
from sqlalchemy.ext.declarative import declarative_base

Device_base = declarative_base()


class Device(Device_base):
    __tablename__ = 'device'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))
    created_at = Column(TIMESTAMP, default=dt.utcnow().timestamp())
