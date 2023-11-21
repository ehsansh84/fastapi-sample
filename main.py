from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi import APIRouter, status, HTTPException, Request
from api_models.sensor import Read, Write, Update, ListRead
from api_models.general import Item, OutputOnlyNote, OutputCreate

app = FastAPI()


sensors = []


@app.post("/sensor/", status_code=status.HTTP_201_CREATED, response_model=OutputCreate)
async def create_item(item: Write):
    sensors.append(item)
    return {"data": {"uid": item.uid}, "detail": "Item successfully created."}


@app.get("/sensor/", status_code=status.HTTP_200_OK, response_model=ListRead)
async def read_item():
    return sensors


@app.get("/sensor/{uid}", status_code=status.HTTP_200_OK, response_model=Read)
async def read_item(uid: str):
    for item in sensors:
        if item.uid == uid:
            return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Record not found!',
    )


@app.put("/sensor/{uid}", status_code=status.HTTP_201_CREATED)
async def update_item(uid: str, item: Update):
    print(sensors)
    temp = Write()
    vars(temp).update(vars(item))
    temp.uid = uid
    # item.uid = uid
    for idx, sensor in enumerate(sensors):
        if sensor.uid == uid:
            # sensors[idx] = item
            sensors[idx] = temp
            return 'Item successfully updated.'
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Record not found!',
    )


# @app.delete("/sensor/{uid}", status_code=status.HTTP_200_OK, response_model=OutputOnlyNote)
@app.delete("/sensor/{uid}", status_code=status.HTTP_200_OK)
async def delete_item(uid: str):
    for item in sensors:
        if item.uid == uid:
            print(sensors)
            sensors.remove(item)
            print(sensors)
            return 'Item successfully deleted.'

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Record not found!',
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
