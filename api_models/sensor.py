import uuid
from pydantic import BaseModel, Field
from typing import List
from enum import Enum


class SensorStatus(str, Enum):
    Active = "active"
    Inactive = "inactive"


class Base(BaseModel):
    f"""
    Use this model for base fields of a Sensor
    """
    name: str = ""
    status: SensorStatus = SensorStatus.Inactive
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
    pass

ListRead = List[Read]
