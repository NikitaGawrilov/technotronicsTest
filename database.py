from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.pool import NullPool

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base = declarative_base()

metadata = MetaData()

engine = create_async_engine(DATABASE_URL, poolclass=NullPool)
session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session():
    async with session_maker() as session:
        yield session
