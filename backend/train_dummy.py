import torch
from ai.model import QuantumLSTMGNN

# Initialize model
model = QuantumLSTMGNN(input_dim=14, hidden_dim=512)

# Save dummy weights
torch.save(model.state_dict(), 'models/pretrained/quantum_gnn.pt')
print("Dummy model weights saved!")