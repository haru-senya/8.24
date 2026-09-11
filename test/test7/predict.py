import torch
from torch import nn


model = nn.Linear(1,1)

model.load_state_dict(
    torch.load("model.pt")
)

model.eval()


x = torch.tensor([[5.]])

with torch.no_grad():

    y = model(x)

    print(y)