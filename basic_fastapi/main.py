from fastapi import FastAPI
items_id =0
app = FastAPI()

@app.get('/')
def home():
  return {"Message " : " All days is good"}

@app.get('/items/{items_id}')
def items():
  return items_id