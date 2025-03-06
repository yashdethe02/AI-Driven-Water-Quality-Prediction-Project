from fastapi import APIRouter
router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

from fastapi import APIRouter, WebSocket
from ai.model import QuantumLSTMGNN
import torch

router = APIRouter()

# Initialize model first
model = QuantumLSTMGNN(input_dim=14, hidden_dim=512)

# Then load weights
model.load_state_dict(
    torch.load(
        "models/pretrained/quantum_gnn.pt",
        map_location=torch.device('cpu'),
        weights_only=True
    )
)
model.eval()

@router.get("/predict-test")
async def test_prediction():
    dummy_input = torch.randn(1, 14)  # Match input_dim
    with torch.no_grad():
        output = model(dummy_input)
    return {"prediction": output.tolist()}

@router.get("/health")  # Must have this exact decorator
async def health_check():
    return {"status": "healthy", "model_loaded": True}
