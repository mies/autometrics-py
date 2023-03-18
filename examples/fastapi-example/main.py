from typing import Union

from fastapi import FastAPI
from autometrics.autometrics import autometrics
from prometheus_client import start_http_server

app = FastAPI()

@autometrics
@app.get("/")
async def read_root():
    do_something()
    return {"Hello": "World"}

start_http_server(8080)

# looking up this function in prometheus works
@autometrics
def do_something():
    print("done")

help(do_something)
