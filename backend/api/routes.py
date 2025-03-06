from fastapi import APIRouter, WebSocket
from ai.model import QuantumLSTMGNN
import torch
import numpy as np

router = APIRouter()

model = QuantumLSTMGNN().eval()
model.load_state_dict(torch.load('models/pretrained/quantum_gnn.pt'))

@router.websocket("/ws/advanced-predict")
async def realtime_prediction(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        tensor = torch.FloatTensor(data['features'])
        edge_index = torch.LongTensor(data['edge_index'])
        
        with torch.no_grad():
            prediction = model(tensor, edge_index)
            confidence = torch.softmax(prediction, dim=1).max().item()
        
        await websocket.send_json({
            "prediction": prediction.numpy().tolist(),
            "confidence": confidence,
            "explanation": generate_shap_explanation(tensor)
        })