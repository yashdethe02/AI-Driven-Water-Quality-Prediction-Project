# backend/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router as api_router
from config import settings
import torch
from ai.model import QuantumLSTMGNN 

@asynccontextmanager
async def lifespan(app: FastAPI):
    await load_model()
    yield

app = FastAPI(
    lifespan=lifespan,
    title="WaterGuard API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "WaterGuard API"}

async def load_model():
    try:
        app.state.model = QuantumLSTMGNN(input_dim=14, hidden_dim=512)
        app.state.model.load_state_dict(
            torch.load(
                settings.MODEL_PATH,
                map_location=torch.device('cpu'),
                weights_only=True
            )
        )
        app.state.model.eval()
        print("✅ Model loaded successfully")
    except Exception as e:
        print(f"❌ Model loading failed: {str(e)}")
        raise

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "WaterGuard Prediction API",
        "docs": "/api/docs",
        "health_check": "/api/v1/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)