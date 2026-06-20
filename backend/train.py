import torch
from model import Bigram, get_batch

max_iters = 5000
eval_interval = 300
device = 'cuda' if torch.cuda.is_available() else 'cpu'
lr = 3e-3
eval_iters = 200

model = Bigram()
m = model.to(device)
optimizer = torch.optim.AdamW(m.parameters(), lr=lr)

@torch.no_grad()
def estimate_loss():
    out = {}
    model.eval()
    for split in ['train', 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            X, Y = get_batch(split)
            logits, loss = model(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()

    model.train()
    return out

if __name__ == "__main__":
    for iter in range(max_iters):
        if iter%eval_interval == 0:
            losses = estimate_loss()
            print(f"{iter}: train loss is {losses['train']} and val loss is {losses['val']}")
        xb, yb = get_batch('train')
        logits, loss = m(xb, yb)
        optimizer.zero_grad(set_to_none = True)
        loss.backward()
        optimizer.step()
    torch.save(model.state_dict(), 'model_weights.pth')
