from fastapi import FastAPI, Query
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from inference import infer
from fastapi.responses import StreamingResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/rap")
def rap(max_tokens : int = Query(100)):
    return StreamingResponse(infer(max_tokens), media_type="text/plain")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)