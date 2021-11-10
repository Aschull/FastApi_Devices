from fastapi import FastAPI
from models.models import init_db, Dispositivos
from resource import device
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


init_db()
app.include_router(device.router)
