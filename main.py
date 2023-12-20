from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from executer import executer
app = FastAPI()
@app.post("/webhook")
async def root(request: Request):
    data = await request.json()
    print(data)
    executer(data)
    return JSONResponse(content=data)
