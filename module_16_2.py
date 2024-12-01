from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def main_page() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin_page() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_page(user_id: Annotated[int, Path(gt=0, le=100, title="Enter User ID", example=10)]) -> str:
    return f'Вы вошли как пользователь №{user_id}'

@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, title="Enter username", example="UrbanUser")],
                    age: Annotated[int, Path(gt=17, le=120, title="Enter age", example="19")]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"