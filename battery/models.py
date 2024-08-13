from sqlalchemy import Integer, VARCHAR, TIMESTAMP, Column, ForeignKey
from datetime import datetime as dt
from sqlalchemy.ext.declarative import declarative_base
from device.models import Device


Battery_base = declarative_base()


class Battery(Battery_base):
    __tablename__ = 'battery'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))
    paired_device_id = Column(Integer, ForeignKey(Device.id, ondelete='SET NULL'))
    created_at = Column(TIMESTAMP, default=dt.utcnow)
