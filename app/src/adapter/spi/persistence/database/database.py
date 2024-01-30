import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session, Session
from sqlalchemy.ext.declarative import declarative_base
from src.config.settings_config import settings
from src.core.util.logger_custom import Logger


## from sqlalchemy.ext.asyncio import create_async_engine
## from sqlalchemy.ext.asyncio import AsyncEngine
## from sqlalchemy.ext.asyncio import AsyncSession

# __engine = create_engine(settings.DB_BASE_URL, connect_args={"check_same_thread": False})

__engine = create_engine(url=f"{settings.DB_DRIVER}:///{settings.DB_BASE_URL}", pool_size=10, max_overflow=20, future=True)

Base = declarative_base()

SessionLocal: Session = sessionmaker(
    autocommit=False, 
    autoflush=False,
    bind=__engine
)

def __openSessionScopped() -> Session:
    sessionScopedDB = scoped_session(SessionLocal)
    try:
        yield sessionScopedDB
    finally:
        Logger.info(Logger.getClassMethodCurrent(), "Done session")
        sessionScopedDB.close()

def getSession() -> Session:
    return next(__openSessionScopped())

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

