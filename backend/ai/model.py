import torch
import torch.nn as nn
from torch_geometric.nn import GATv2Conv, global_max_pool

class QuantumLSTMGNN(nn.Module):
    def __init__(self, input_dim=14, hidden_dim=512):
        super().__init__()
        self.gnn1 = GATv2Conv(input_dim, hidden_dim, heads=4)
        self.gnn2 = GATv2Conv(hidden_dim*4, hidden_dim, heads=2)
        self.lstm = nn.LSTM(hidden_dim*2, hidden_dim, bidirectional=True)
        self.quantum_layer = nn.Sequential(
            nn.Linear(hidden_dim*2, hidden_dim*4),
            nn.ELU(),
            nn.Dropout(0.3),  # Added comma
        )  # Added closing parenthesis
        self.classifier = nn.Linear(hidden_dim*4, 5)  # 5 water quality classes

    def forward(self, x, edge_index, batch=None):
        x = torch.relu(self.gnn1(x, edge_index))
        x = torch.relu(self.gnn2(x, edge_index))
        x, _ = self.lstm(x.unsqueeze(1))
        x = self.quantum_layer(x.squeeze(1))
        return self.classifier(x)