from fastapi import FastAPI

app = FastAPI()


@app.get("/async_hello")
async def get_async_hello():
    return {"hello": "world"}
