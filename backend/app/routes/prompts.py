from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..database import AsyncSessionLocal
from ..models import Prompt
from ..schemas import PromptCreate, PromptOut
from ..core.llm import execute_prompt
import uuid

router = APIRouter(prefix="/api/v1/prompts", tags=["prompts"])

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/", response_model=PromptOut)
async def create_prompt(data: PromptCreate, db: AsyncSession = Depends(get_db)):
    prompt = Prompt(id=str(uuid.uuid4()), **data.model_dump())
    db.add(prompt)
    await db.commit()
    await db.refresh(prompt)
    return prompt

@router.get("/", response_model=list[PromptOut])
async def list_prompts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Prompt).order_by(Prompt.updated_at.desc()))
    return result.scalars().all()

@router.post("/{prompt_id}/execute")
async def execute(prompt_id: str, variables: dict):
    return await execute_prompt(prompt_id, variables)
