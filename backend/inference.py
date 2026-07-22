import torch
from model import Bigram, decode
from pathlib import Path
import time

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# create a NEW model instance
model = Bigram()
model.load_state_dict(torch.load(Path(__file__).with_name("model_weights.pth"), map_location=device))

model.to(device)
model.eval()


def infer(max_new_tokens):
    for token in model.generate(torch.zeros((1,1), dtype = torch.long, device = device), max_new_tokens=max_new_tokens):
        start = time.time()
        yield token
        print("time after generating the first set of tokens...", time.time()-start)
