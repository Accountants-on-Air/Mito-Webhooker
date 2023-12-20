from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from monday import MondayClient
import json
app = FastAPI()
client = MondayClient('eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjIyMDI0MjExNSwiYWFpIjoxMSwidWlkIjozNzc5MjU0MCwiaWFkIjoiMjAyMy0wMS0xMFQxNjowNzoxNS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6NjkwOTQ3NCwicmduIjoidXNlMSJ9.ZiE5WtSS3eW5NgNLoOO7jHrDZvRBHMmmNApWhnfRIhk')
@app.post("/webhook")
async def root(request: Request):
    data = await request.json()
    # query = json.loads('{{\"connect_boards1\" : {{\"item_ids\" : {}}}}}'.format(data['event']['pulseId']))
    #client.items.change_multiple_column_values(5015701381,data['event']['value']['linkedPulseIds'][0]['linkedPulseId'],query)
    return JSONResponse(content=data)
