import uvicorn
from fastapi import FastAPI

from src.routers import full_routers


app = FastAPI()
app.include_router(full_routers)

HOST = "0.0.0.0"
PORT = 8000


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
