#
# SAMPLE based on https://cloud.google.com/apis/design
#
# Routes for a **collection** of items
#

import logging
from typing import List, Optional

from fastapi import APIRouter, Body, Depends, HTTPException, Query
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_409_CONFLICT,
    HTTP_501_NOT_IMPLEMENTED,
)

from ...db.repositories.items import ItemsRepository
from ...models.schemas.items import ItemCreate, ItemDetailed, ItemOverview, ItemUpdate
from ..dependencies.database import get_repository

router = APIRouter()


log = logging.getLogger(__name__)


@router.get("", response_model=List[ItemOverview])
async def list_items(
    page_token: Optional[str] = Query(
        None, description="Requests a specific page of the list results"
    ),
    page_size: int = Query(
        0, ge=0, description="Maximum number of results to be returned by the server"
    ),
    order_by: Optional[str] = Query(
        None, description="Sorts in ascending order comma-separated fields"
    ),
    items_repo: ItemsRepository = Depends(get_repository(ItemsRepository)),
):

    # List is suited to data from a single collection that is bounded in size and not cached

    # Applicable common patterns
    # SEE pagination: https://cloud.google.com/apis/design/design_patterns#list_pagination
    # SEE sorting https://cloud.google.com/apis/design/design_patterns#sorting_order

    # Applicable naming conventions
    # TODO: filter: https://cloud.google.com/apis/design/naming_convention#list_filter_field
    # SEE response: https://cloud.google.com/apis/design/naming_convention#list_response
    log.debug("%s %s %s", page_token, page_size, order_by)
    items = await items_repo.list_not_detailed()
    return items


@router.get(":batchGet")
async def batch_get_items():
    raise HTTPException(
        status_code=HTTP_501_NOT_IMPLEMENTED, detail="Still not implemented"
    )


@router.get(":search")
async def search_items():
    # A method that takes multiple resource IDs and returns an object for each of those IDs
    # Alternative to List for fetching data that does not adhere to List semantics, such as services.search.
    # https://cloud.google.com/apis/design/standard_methods#list
    raise HTTPException(
        status_code=HTTP_501_NOT_IMPLEMENTED, detail="Still not implemented"
    )


@router.get("/{item_id}", response_model=ItemDetailed)
async def get_item(
    item_id: int,
    items_repo: ItemsRepository = Depends(get_repository(ItemsRepository)),
):
    item = await items_repo.get_item(item_id)
    return item


@router.post(
    "",
    response_model=int,
    status_code=HTTP_201_CREATED,
    response_description="Successfully created",
)
async def create_item(
    item: ItemCreate = Body(...),
    items_repo: ItemsRepository = Depends(get_repository(ItemsRepository)),
):
    assert item  # nosec

    if item.version == "0.0.0" and item.key == "foo":
        # client-assigned resouce name
        raise HTTPException(
            status_code=HTTP_409_CONFLICT,
            detail=f"item {item.key}:{item.version} already exists",
        )

    # FIXME: conversion item (issue with workbench being json in orm and dict in schema)
    item_id = await items_repo.create_item(item)
    # TODO: no need to return since there is not extra info?, perhaps return
    return item_id


@router.patch("/{item_id}", response_model=ItemDetailed)
async def udpate_item(
    item_id: int,
    item: ItemUpdate = Body(None),
    items_repo: ItemsRepository = Depends(get_repository(ItemsRepository)),
):
    async with items_repo.connection.begin():
        await items_repo.update_item(item_id, item)
        updated_item = await items_repo.get_item(item_id)

    return updated_item


@router.put("/{item_id}", response_model=Optional[ItemDetailed])
async def replace_item(
    item_id: int,
    item: ItemCreate = Body(...),
    items_repo: ItemsRepository = Depends(get_repository(ItemsRepository)),
):
    await items_repo.replace_item(item_id, item)


@router.delete(
    "/{item_id}",
    status_code=HTTP_204_NO_CONTENT,
    response_description="Successfully deleted",
)
async def delete_item(
    item_id: int,
    items_repo: ItemsRepository = Depends(get_repository(ItemsRepository)),
):
    # If the Delete method immediately removes the resource, it should return an empty response.
    # If the Delete method initiates a long-running operation, it should return the long-running operation.
    # If the Delete method only marks the resource as being deleted, it should return the updated resource.
    await items_repo.delete_item(item_id)
