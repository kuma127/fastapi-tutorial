from fastapi import FastAPI

app = FastAPI()


async def asgi_app(scope, receive, send):
    event = await receive()
    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [[b"content-type", b"text/plain"]]
    })
    await send({
        "type": "http.response.body",
        "body": event["body"]
    })
