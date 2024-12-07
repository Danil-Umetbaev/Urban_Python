from fastapi import FastAPI, Path, HTTPException, status
from typing import Annotated, List
from pydantic import BaseModel, ValidationError, validator

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
async def append_user(
    username: Annotated[str, validator(min_length=3, max_length=20)],
    age: Annotated[int, validator(min_value=0, max_value=120)],
):
    new_id = max((user.id for user in users), default=0) + 1
    try:
        new_user = User(id=new_id, username=username, age=age)
        users.append(new_user)
        return {"message": f"{new_user} was created!", "user": new_user}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))



@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: int,
    username: Annotated[str, validator(min_length=3, max_length=20)],
    age: Annotated[int, validator(min_value=0, max_value=120)],
):
    try:
        for i, u in enumerate(users):
            if u.id == user_id:
                users[i] = User(id=user_id, username=username, age=age)
                return {"message": f"{users[i]} was updated!", "user": users[i]}
        raise HTTPException(status_code=404, detail="User not found")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u.id == user_id:
            deleted_user = users.pop(i)
            return {"message": f"{deleted_user} was deleted!"}
    raise HTTPException(status_code=404, detail="User not found")
