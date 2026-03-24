import random

import redis
from fastapi import FastAPI
import uvicorn
from starlette.responses import RedirectResponse, HTMLResponse

app = FastAPI()

# 连接 Redis
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def convert(num: int) -> str:
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    res = []
    if num == 0:
        return chars[0]

    while num:
        num, rem = divmod(num, len(chars))
        res.append(chars[rem])

    return ''.join(reversed(res))


@app.get("/", response_class=HTMLResponse)
def generate_short_url():
    short_id = r.incr("short_url:id")
    short = convert(short_id)
    short_url = f"http://127.0.0.1:8000/{short}"
    return f"""
    <html>
        <body>
            <h2>Short URL Generated:</h2>
            <a href="{short_url}">{short_url}</a>
        </body>
    </html>
    """


@app.get("/{short_path}")
def redirect_to(short_path: str):
    if len(short_path) % 2 == 0:
        url = "https://baidu.com"
    else:
        url = "http://jd.com"
    return RedirectResponse(status_code=302, url=url)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
