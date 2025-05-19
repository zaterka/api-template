from typing import List

from fastapi import APIRouter, HTTPException, status

from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.services.item_service import item_service

router = APIRouter()


@router.get("/items", response_model=List[Item], tags=["Items"])
async def read_items():
    """
    Get all items.
    """
    return item_service.get_items()


@router.get("/items/{item_id}", response_model=Item, tags=["Items"])
async def read_item(item_id: int):
    """
    Get an item by ID.
    """
    item = item_service.get_item(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found",
        )
    return item


@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
async def create_item(item: ItemCreate):
    """
    Create a new item.
    """
    return item_service.create_item(item)


@router.put("/items/{item_id}", response_model=Item, tags=["Items"])
async def update_item(item_id: int, item: ItemUpdate):
    """
    Update an existing item.
    """
    updated_item = item_service.update_item(item_id, item)
    if updated_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found",
        )
    return updated_item


@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
async def delete_item(item_id: int):
    """
    Delete an item.
    """
    deleted = item_service.delete_item(item_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found",
        )
    return None 