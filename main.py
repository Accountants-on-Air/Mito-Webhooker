from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from executer import executer,executer2
app = FastAPI()
@app.post("/webhook") #Master Database
async def root(request: Request):
    data = await request.json()
    if (len(data) > 0):
        if (data['event']['groupId'] != 'leads_'):
            print(data)
            executer(data)
    return JSONResponse(content=data)

@app.post("/webhook2") #Tax Prep Assignmetns
async def root(request: Request):
    data = await request.json()
    print(data)
    executer2(data)
    return JSONResponse(content=data)

@app.post("/webhook3") #Dwidar Stamp HR
async def root(request: Request):
    data = await request.json()
    print(data)
    #executer3(data)
    return JSONResponse(content=data)
