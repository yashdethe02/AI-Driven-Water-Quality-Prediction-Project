import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_PATH: str = os.getenv("MODEL_PATH", "models/pretrained/quantum_gnn.pt")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    CACHE_EXPIRATION: int = 3600  # 1 hour

settings = Settings()