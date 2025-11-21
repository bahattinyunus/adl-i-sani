from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="AI & HUKUK — Geleceğin Adalet Laboratuvarı"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to AI & Law - The Future of Justice",
        "vision": "Adalet gecikmez, otomatikleşir.",
        "modules": [
            "Smart Contract Analyzer",
            "Legislation Radar 2.0",
            "Case Law Search Engine",
            "Explainable Justice Engine",
            "Ethics & Audit Forge"
        ]
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": settings.PROJECT_VERSION}
