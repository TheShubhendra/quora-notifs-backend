from fastapi import FastAPI
from quora import User


app = FastAPI()

@app.get("/")
async def home():
    return {"message":"Welcome to quora notifs"}


@app.get("/getProfile/{username}")
async def getProfile(username: str):
    user = User(username)
    profile = await user.profile()
    return profile.json()


