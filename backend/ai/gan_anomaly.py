import torch
import torch.nn as nn

class AnomalyGAN(nn.Module):
    def __init__(self, input_dim=10):
        super().__init__()
        self.generator = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.LeakyReLU(0.2),
            nn.Linear(128, 256),
            nn.Tanh()
        )
        self.discriminator = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def detect_anomaly(self, x):
        generated = self.generator(x)
        error = torch.mean((x - generated)**2, dim=1)
        return error > 0.5  # Threshold