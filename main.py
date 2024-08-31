from functools import wraps
import json
from fastapi import FastAPI
import os
import logging

def load_mock_data():
    with open("mock.json", "r") as f:
        return json.load(f)


API_ENV = os.getenv("API_ENV", "develop")

if API_ENV != "production":
    from dotenv import load_dotenv

    load_dotenv()
    mock_data = load_mock_data() if API_ENV != "production" else {}

app = FastAPI()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def use_mock_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if API_ENV != "production":
            func_name = func.__name__
            return mock_data.get(func_name, [])
        return func(*args, **kwargs)

    return wrapper


@app.get("/teacher")
@use_mock_data
def read_teacher():
    # do some third party API call

    return {"_id": "w12345", "name": "Nijia"}


@app.get("/student")
@use_mock_data
def read_student(student_id: str):
    return {
        "_id": student_id,
        "total_member": len([0, 1, 2]),
        "rating": 1,
        "query_list": [{"a": 1}, {"b": 2}],
    }


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", default=8000))
    # activate debug mode when developer mode is on
    debug = True if os.environ.get("API_ENV", default="develop") == "develop" else False
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
