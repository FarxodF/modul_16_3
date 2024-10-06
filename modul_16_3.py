from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
def get_users():
    return users


@app.post("/user/{username}/{age}")
def create_user(
        username: Annotated[str, Path(description="Enter username", min_length=5, max_length=20)],
        age: Annotated[int, Path(description="Enter age", ge=18, le=120)]
):
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
def update_user(
        user_id: Annotated[int, Path(description="Enter User ID", ge=1)],
        username: Annotated[str, Path(description="Enter username", min_length=5, max_length=20)],
        age: Annotated[int, Path(description="Enter age", ge=18, le=120)]
):
    if str(user_id) in users:
        users[str(user_id)] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    else:
        return f"User {user_id} not found"


@app.delete("/user/{user_id}")
def delete_user(
        user_id: Annotated[int, Path(description="Enter User ID", ge=1)]
):
    if str(user_id) in users:
        del users[str(user_id)]
        return f"User {user_id} has been deleted"
    else:
        return f"User {user_id} not found"
