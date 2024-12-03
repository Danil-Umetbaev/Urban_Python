from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

    def __str__(self):
        return f'User {self.id}, username: {self.username}, age: {self.age}'

@app.get("/users")
async def get_all_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def append_user(username: str, age: int) -> str:
    new_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return str(new_user) + " was created!"



@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:

    for i in range(len(users)):
        if users[i].id == user_id:
            users[i] = User(id=user_id, username=username, age=age)
            return str(User) + " was updated!"
    raise HTTPException(status_code=404, detail="Такого пользоваетля нет(")

@app.delete("/user/{user_id}")
async def delete_message(user_id: int) -> str:
    for i in range(len(users)):
        if users[i].id == user_id:
            del users[i]
            return f'User id {user_id} was deleted!'

    raise HTTPException(status_code=404, detail="Такого пользоваетля нет(")