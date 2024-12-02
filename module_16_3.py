from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_all_users() -> dict:
    return users
@app.post("/user/{username}/{age}")
async def append_user(username: Annotated[str, Path(min_length=3, max_length=20, title="Enter username", example="Danil")],
                      age: Annotated[int, Path(gt=17, le=120, title="Enter age", example="19")]) -> str:
    new_id = max(int(user) for user in users.keys()) + 1 if users else 1
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f"User {new_id} is registered"



@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int,
        username: Annotated[str, Path(min_length=3, max_length=20, title="Enter username", example="Danil")],
                      age: Annotated[int, Path(gt=17, le=120, title="Enter age", example="19")]) -> str:
    user_id = str(user_id)
    if user_id in users.keys():
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f"The user {user_id} is updated"
    else:
        raise HTTPException(status_code=404, detail="Такого пользоваетля нет(")

@app.delete("/user/{user_id}")
async def delete_message(user_id: int) -> str:
    user_id = str(user_id)
    if user_id in users.keys():
        users.pop(user_id)
        return f"User with {user_id} was deleted"
    else:
        raise HTTPException(status_code=404, detail="Такого пользоваетля нет(")
