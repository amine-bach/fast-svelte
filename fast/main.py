from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()

# https://css-tricks.com/what-i-like-about-writing-styles-with-svelte/
app.mount("/svelte", StaticFiles(directory="svelte/public", html=True), name="svelte")
app.mount(
    "/built-svelte", StaticFiles(directory="svelte/public/build"), name="built-svelte"
)


@app.get("/toto")
async def root():
    return {"message": "ok"}


@app.get("/")
async def svelte():
    return RedirectResponse(url="svelte")
