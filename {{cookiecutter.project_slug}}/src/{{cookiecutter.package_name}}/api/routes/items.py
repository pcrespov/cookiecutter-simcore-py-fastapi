#
# TODO: use this example as template for CRUD on a resource
#

from typing import List

from fastapi import APIRouter, Depends, FastAPI, HTTPException, Query

router = APIRouter()

# CRUD operations on items


@router.get("", response_model=List[schemas.Item])
async def read_items(skip: int = Query(0, gt=0), limit: int = 100):
    items = await crud.get_items(conn, skip=skip, limit=limit)
    return items

