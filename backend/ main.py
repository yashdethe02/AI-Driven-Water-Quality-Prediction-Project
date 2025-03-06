# backend/main.py
import torch
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai.model import QuantumLSTMGNN
from api.routes import router as api_router
from config import settings

app = FastAPI(
    title="WaterGuard API",
    description="Advanced Water Quality Prediction System",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ML model on startup
@app.on_event("startup")
async def load_model():
    try:
        # Initialize model
        app.state.model = QuantumLSTMGNN(
            input_dim=14, 
            hidden_dim=512
        )
        
        # Load trained weights
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
        print(f"❌ Failed to load model: {str(e)}")
        raise RuntimeError("Model initialization failed") from e

# Include API routes
app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        log_level="debug"
    )