from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from executer import executer
app = FastAPI()
@app.post("/webhook") #Master Database
async def root(request: Request):
    data = await request.json()
    print(data)
    executer(data)
    return JSONResponse(content=data)

@app.post("/webhook2")
async def root(request: Request):
    data = await request.json()
    print(data)
    return JSONResponse(content=data)