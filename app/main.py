import os
import structlog

from sqlalchemy.ext.asyncio import create_async_engine

from api import BudiAPI
from application import BudiApplication
from repository import BudiRepository

POSTGRES_DB_SERVER = os.getenv("POSTGRES_DB_SERVER", "localhost")
POSTGRES_DB_PORT = os.getenv("POSTGRES_DB_PORT", "5434")
POSTGRES_DB_API_USER = os.getenv("POSTGRES_DB_API_USER", "javan_user")
POSTGRES_DB_API_PASSWORD = os.getenv("POSTGRES_DB_API_PASSWORD", "javan_password")
POSTGRES_DB_API = os.getenv("POSTGRES_DB_API", "javan_development")
POSTGRES_DB_URI = f"postgresql+asyncpg://{POSTGRES_DB_API_USER}:{POSTGRES_DB_API_PASSWORD}@{POSTGRES_DB_SERVER}:{POSTGRES_DB_PORT}/{POSTGRES_DB_API}"

engine = create_async_engine(
    POSTGRES_DB_URI,
    echo=False,  # set it to True if you wanna know what sqlalchemy did
    pool_size=100,
    max_overflow=200,
    pool_recycle=300,
    pool_pre_ping=True,
    pool_use_lifo=True,
)

logger = structlog.get_logger("budi")

repo = BudiRepository(engine, logger)
app = BudiApplication(repo,logger)
api = BudiAPI(app)