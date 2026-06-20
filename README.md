# rapgpt

Character-level decoder-only [Transformer](https://arxiv.org/pdf/1706.03762) (no cross-attention) trained on Eminem songs using the [kaggle](https://www.kaggle.com/datasets/thaddeussegura/eminem-lyrics-from-all-albums/data) dataset.

<div align="center">
  <img src="assets/logo.png" alt="logo" width="700" height = "500"style="margin-right: 20px;">
  <img src="assets/transformers.jpg" alt="transformers" width="400" style="margin-left: 20px;">
</div>

Requirements
------------
- Python 3.8 or newer.
- PyTorch

Usage
-----
### clone the repository:
```
git clone https://github.com/nithinbharathi/rapgpt.git
cd rapgpt
```
### Run backend:
```
cd backend
python -m env env
pip install torch
pip install fastapi
pip install uvicorn
```

### Run frontend:
```
cd frontend
npm install
npm run dev
```

<div align="center">
<img src="assets/loss_curve.png" alt = "alt" width="700">
<p><b>Figure 1: Model Loss over epochs</b></p>
</div>

<div align="center">
<img src="assets/rapgpt.jpg" alt = "alt" width="700">
<p><b>Figure 2: front end</b></p>
</div>



Acknowledgements
-------------------
Inspired by Andrej Karpathy's [nanoGPT](https://github.com/karpathy/nanoGPT) and his [youtube gpt lecture](https://www.youtube.com/watch?v=kCc8FmEb1nY).