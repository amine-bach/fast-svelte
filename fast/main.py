from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()

# https://css-tricks.com/what-i-like-about-writing-styles-with-svelte/
app.mount("/front", StaticFiles(directory="front/public", html=True), name="front")
app.mount("/build", StaticFiles(directory="front/public/build"), name="build")


@app.get("/toto")
async def root():
    return {"message": "ok"}


@app.get("/")
async def front():
    return RedirectResponse(url="front")
