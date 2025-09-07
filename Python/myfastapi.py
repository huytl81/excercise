# pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()

# chay lenh: uvicorn myfastapi:app --reload
@app.get("/users/{user_id}") # route decorator
async def get_user(user_id):
    return {"user_id": user_id}

@app.get("/search")
async def search_user(name, age=None):
    return {"name": name, "age": age}
