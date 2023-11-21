import uuid
from pydantic import BaseModel, Field
from typing import List


class Base(BaseModel):
    f"""
    Use this model for base fields of a Sensor
    """
    name: str = ""
    status: str = ""
    location: dict = {}

    def __init__(self, **data):
        super().__init__(**data)

    def __str__(self):
        attributes = vars(self)
        return ", ".join(f"{key}: {value}" for key, value in attributes.items())


class Write(Base):
    f"""
    Use this model to create a Sensor
    """
    uid: str = Field(description="uid of Sensor", example="f969d7c6-c9a0-470b-84bf-b286f71ca38b", default=str(uuid.uuid4()))


class Read(Base):
    f"""
    Use this model to read a Sensor
    """
    uid: str = Field(description="uid of Sensor", example="f969d7c6-c9a0-470b-84bf-b286f71ca38b")


class Update(Base):
    f"""
    Use this model to update a Sensor
    """
    # In case of a real database we do not need this field
    uid: str = Field(description="uid of Sensor", example="f969d7c6-c9a0-470b-84bf-b286f71ca38b")


ListRead = List[Read]
