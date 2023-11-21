from fastapi import FastAPI
import uvicorn
import uuid
from pydantic import BaseModel


app = FastAPI()


sensors = []


class Sensor(BaseModel):
    uid: str = ""
    name: str = ""
    status: str = ""
    location: dict = {}

    def __init__(self, **data):
        super().__init__(**data)
        self.uid = str(uuid.uuid4())

    def __str__(self):
        attributes = vars(self)
        return ", ".join(f"{key}: {value}" for key, value in attributes.items())


@app.post("/sensor/")
async def create_item(item: Sensor):
    sensors.append(item)
    print(sensors)
    return {"id": item.uid}


@app.get("/sensor/")
async def read_item():
    return sensors


@app.get("/sensor/{uid}")
async def read_item(uid: str):
    for item in sensors:
        if item.uid == uid:
            return item
    return {}


@app.put("/sensor/{uid}")
async def update_item(uid: str, item: Sensor):
    print(item.uid)
    return {}


@app.delete("/sensor/{uid}")
async def delete_item(uid: str):
    for item in sensors:
        if item.uid == uid:
            sensors.remove(item)
    print(sensors)
    return 1


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
