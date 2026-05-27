from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routes import prompts
from .database import engine
from .models import Base

app = FastAPI(title="PromptForge API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(prompts.router)

@app.get("/api/v1/health")
def health():
    return {"status": "ok", "service": "promptforge-backend"}

@app.get("/api/v1/metrics")
def metrics():
    return {"prompts": 24, "requests": 3487, "cost": 12.40, "latency": 142}
