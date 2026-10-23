import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.models import Snippet

async def create_snippet(db: AsyncSession, title: str, code: str, user_id: int):
    new_snippet = Snippet(uuid=str(uuid.uuid4()), title=title, code=code, owner_id=user_id)
    db.add(new_snippet)
    await db.commit()
    await db.refresh(new_snippet)
    return new_snippet

async def get_snippet_by_uuid(db: AsyncSession, snippet_uuid: str):
    result = await db.execute(select(Snippet).where(Snippet.uuid == snippet_uuid))
    return result.scalar_one_or_none()