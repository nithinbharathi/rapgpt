import torch
from model import Bigram, decode

max_new_tokens = 1000
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# create a NEW model instance
model = Bigram()

# load trained weights
model.load_state_dict(torch.load("model_weights.pth"))

model.to(device)
model.eval()

print(decode(model.generate(torch.zeros((1,1), dtype = torch.long, device = device), max_new_tokens=max_new_tokens)[0].tolist()))