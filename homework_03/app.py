from fastapi import FastAPI
from pydantic import constr
import random

app = FastAPI()


@app.get("/ping/", status_code=200)
def root():
    return {"message": "pong"}


@app.get("/hello")
def hello(name: constr(min_length=3)):
    return {"message": f"Hello {name}"}


@app.get("/add")
def add(a: int, b: int):
    return {"a": a, "b": b, "sum": a + b}


@app.get("/random")
def random_nums(ar: int, br: int):
    return {"random num": random.randint(ar, br)}
