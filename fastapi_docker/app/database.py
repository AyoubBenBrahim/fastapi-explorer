from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@db:5432/messages_db"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

# Modified database session manager
async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()
