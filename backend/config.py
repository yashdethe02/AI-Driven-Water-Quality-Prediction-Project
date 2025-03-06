import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    model_path: str = os.getenv("MODEL_PATH", "models/pretrained")
    redis_host: str = os.getenv("REDIS_HOST", "redis")
    
    class Config:
        env_file = ".env"

settings = Settings()