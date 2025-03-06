import torch
from pathlib import Path  # Add this import
from ai.model import QuantumLSTMGNN

# Initialize model
model = QuantumLSTMGNN(input_dim=14, hidden_dim=512)

# Create directory if not exists
Path("models/pretrained").mkdir(parents=True, exist_ok=True)

# Save properly
torch.save(model.state_dict(), "models/pretrained/quantum_gnn.pt")
print("✅ New model weights saved successfully!")