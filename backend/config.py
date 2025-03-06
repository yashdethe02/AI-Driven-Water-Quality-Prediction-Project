# backend/config.py
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    MODEL_PATH: str = Field(default="models/pretrained/quantum_gnn.pt")
    REDIS_URL: str = Field(default="redis://redis:6379/0")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()