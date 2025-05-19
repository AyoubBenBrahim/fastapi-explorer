from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel

from .database import get_db, engine
from .models import Message, Base

app = FastAPI()

class MessageCreate(BaseModel):
    content: str

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/messages/")
async def create_message(message: MessageCreate, db: AsyncSession = Depends(get_db)):
    new_message = Message(content=message.content)
    db.add(new_message)
    await db.commit()
    await db.refresh(new_message)
    return new_message

@app.get("/messages/{message_id}")
async def read_message(message_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Message).filter(Message.id == message_id))
    message = result.scalars().first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message

@app.get("/messages/")
async def read_all_messages(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Message))
    messages = result.scalars().all()
    return messages
