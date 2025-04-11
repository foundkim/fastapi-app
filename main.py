"""Main Module"""

from fastapi import FastAPI
import uvicorn

from api import inference_router

from core import config


app = FastAPI(title=config.API_TITLE)


app.include_router(inference_router)


@app.get("/", tags=["Home Page"])
async def root():
    """Default page"""

    return "ML Flow Service"


if __name__ == "__main__":

    uvicorn.run("main:app", host=config.API_HOST, port=config.API_PORT, reload=True)
