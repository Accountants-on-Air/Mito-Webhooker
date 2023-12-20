from fastapi import FastAPI, Path
from pydantic import BaseModel
app = FastAPI()
person = {1: {"mito":"Webhook"}}
class Mito(BaseModel):
	mito: str
@app.get("/")
def index():
	return {"mito":"First Data"}
@app.post("/webhook")
def webhook():
	return'Success',200

