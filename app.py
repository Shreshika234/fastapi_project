from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username : str
    email : str
    
class Poll(BaseModel):
    title : str
    type : str
    is_add_choices_active : bool
    is_voting_active : bool




@app.get("/")
async def root():
    return {"Name" : "Shreshika"}


@app.get("/polls")
async def root(poll):
    return poll


@app.get("/users")
async def root(user :User):
    return user
    

@app.post("/users/")
async def create_user(user:User):
    return user

@app.post("/polls/")
async def create_poll(poll : Poll):
    return poll