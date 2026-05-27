from sqlalchemy import Column, String, Text, DateTime, Integer, Boolean
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(String, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    system_prompt = Column(Text, nullable=False)
    user_template = Column(Text, default="")
    version = Column(String, default="1.0")
    model = Column(String, default="gpt-4-turbo")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class APIKey(Base):
    __tablename__ = "api_keys"
    id = Column(String, primary_key=True)
    provider = Column(String, nullable=False)
    encrypted_key = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
