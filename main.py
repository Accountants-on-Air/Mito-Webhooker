from fastapi import FastAPI, Path
from pydantic import BaseModel
app = FastAPI()
class Mito(BaseModel):
	challenge: str
@app.get("/")
def index():
	return {"mito":"First Data"}
@app.post("/webhook")
async def webhook(text: Mito):	
	print(text.challenge)
	return {'success',200}

