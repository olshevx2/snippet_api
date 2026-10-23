from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from schemas.schemas import SnippetCreate, SnippetResponse
from services import snippets

router = APIRouter()

@router.post("/snippets", response_model=SnippetResponse)
async def create_snippet(snippet: SnippetCreate, db: AsyncSession = Depends(get_db)):
    return await snippets.create_snippet(db, snippet.title, snippet.code, user_id=1)

@router.get("/snippets/{snippet_uuid}", response_model=SnippetResponse)
async def get_snippet(snippet_uuid: str, db: AsyncSession = Depends(get_db)):
    snip = await snippets.get_snippet_by_uuid(db, snippet_uuid)
    if not snip:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snip