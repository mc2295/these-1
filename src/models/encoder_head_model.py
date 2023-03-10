

import torch
import torch.nn as nn
from fastai.vision.all import Flatten

class ModelFromResnet(torch.nn.Module):
    def __init__(self, body, head):
        super(ModelFromResnet, self).__init__()
        self.body, self.head = body, head
        self.siamese_head = False
        self.encoder = nn.Sequential(
            self.body,
            nn.AdaptiveMaxPool2d(output_size=1),
            Flatten(),
            nn.Linear(2048, 256))


    def forward(self, x):
        x = self.encoder(x)
        return self.head(x)
    
class Model(torch.nn.Module):
    def __init__(self, encoder, head, siamese_head):
        super(Model, self).__init__()
        self.siamese_head = siamese_head
        self.encoder, self.head = encoder, head
    def forward(self, x):
        x = self.encoder(x)
        return self.head(x)        