# TODO: split in InData, OutData
# TODO: find commons
# TODO: conversion from/to database's ORM in models.py

from typing import List

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str = None


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
