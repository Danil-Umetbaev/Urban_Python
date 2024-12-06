from fastapi import FastAPI, Path, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int
    username: str
    age: int

    def __str__(self):
        return f'User {self.id}, username: {self.username}, age: {self.age}'

users = [User(id=1, username="UrbanUser", age=19)]

@app.get("/", response_class=HTMLResponse)
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    for i in range(len(users)):
        if users[i].id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": users[i]})
    raise HTTPException(status_code=404, detail="Такого пользоваетля нет(")

@app.post("/user/{username}/{age}")
async def append_user(request: Request, username: str, age: int) -> HTMLResponse:
    new_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse("users.html", {"request": request, "users": users})



@app.put("/user/{user_id}/{username}/{age}")
async def update_user(request: Request, user_id: int, username: str, age: int) -> HTMLResponse:
    for i in range(len(users)):
        if users[i].id == user_id:
            users[i] = User(id=user_id, username=username, age=age)
            return templates.TemplateResponse("users.html", {"request": request, "users": users})
    raise HTTPException(status_code=404, detail="Такого пользоваетля нет(")

@app.delete("/user/{user_id}")
async def delete_message(request: Request, user_id: int) -> HTMLResponse:
    for i in range(len(users)):
        if users[i].id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "users": users})
    raise HTTPException(status_code=404, detail="Такого пользоваетля нет(")