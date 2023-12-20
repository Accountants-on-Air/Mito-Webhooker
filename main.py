from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
app = FastAPI()
@app.post("/webhook")
async def root(request: Request):
    data = await request.json()
    return JSONResponse(content=data)
