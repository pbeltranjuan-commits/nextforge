from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PromptCreate(BaseModel):
    name: str
    system_prompt: str
    user_template: str = ""
    model: str = "gpt-4-turbo"

class PromptOut(BaseModel):
    id: str
    name: str
    system_prompt: str
    version: str
    model: str
    updated_at: datetime

class KeyCreate(BaseModel):
    provider: str
    raw_key: str

class KeyOut(BaseModel):
    id: str
    provider: str
    mask: str
    is_active: bool
