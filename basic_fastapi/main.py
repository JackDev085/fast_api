from fastapi import FastAPI
app = FastAPI()

#First attemps
"""
Import FastAPI.
Create an app instance.
Write a path operation decorator (like @app.get("/")).
Write a path operation function (like def root(): ... above).
Run the development server (like uvicorn main:app --reload).
"""
@app.get('/')
def home():
  return {"Message " : " All days is good"}

@app.get("/items/{item_id}")
def read_item(item_id:int):
  return {"Item id " : item_id}

##Order matters

#The order of endpoints matter

#Imagine that, your need to use a endpoint user with param username
#and use too a dynamic param to acess the user content

#if you use the dyyanmic pararam firts, can call a error 
@app.get("/users/me")
def users_me():
  return {"User" : "Currrent_user"}

@app.get("/users/{username}")
def users_me(username:str):
  return {"User" : username}

#Other example
#The firts incidence of endpoint users be executed
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]