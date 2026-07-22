# rapgpt

A tiny character-level decoder-only [Transformer](https://arxiv.org/pdf/1706.03762) (no cross-attention) trained on Eminem songs using the [kaggle](https://www.kaggle.com/datasets/thaddeussegura/eminem-lyrics-from-all-albums/data) dataset.

## Features

- Generate rap lyrics based on user specified token count
- Configurable maximum number of generated tokens

## Project Structure

backend/
- train.py – trains the Transformer model
- inference.py – loads the trained model and runs inference
- model_weights.pth – pretrained model weights
- main.py - starts the backend server and exposes the api

frontend/
- React application

## Requirements
- Python 3.8 or newer
- PyTorch
- Fast API
- Node.js
- React

## Usage

### clone the repository:
```
git clone https://github.com/nithinbharathi/rapgpt.git
cd rapgpt
```
### Run backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Run frontend:
```bash
cd frontend
npm install
npm run dev
```

## Pretrained Model

The repository already includes `backend/model_weights.pth`, so you can run the application immediately without training the model.

## Training (Optional)

If you'd like to train the model yourself,

```bash
cd backend
python train.py
```

The trained model will be saved as

```
model_weights.pth
```

which is automatically loaded by the backend during inference.

## Screenshots

<div align="center">
<img src="assets/output.png" alt = "alt" height = "350" width="700">
<p><b>Figure 1: front end</b></p>
</div>


<div align="center">
<img src="assets/loss_curve.png" alt = "alt" width="700">
<p><b>Figure 2: Model Loss over epochs</b></p>
</div>



## Note About Response Time

This [application](https://rapgpt-lemon.vercel.app/) is deployed on a serverless platform. If the app has not received any requests for a while, the first request may take a little longer to process due to server initialization (cold start).

Subsequent requests will be significantly faster once the server is active.

If you experience a longer-than-usual wait on your first request, please wait a few seconds and try again — the application is warming up.

Acknowledgements
-----------------
Inspired by Andrej Karpathy's [nanoGPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) and related educational resources.
