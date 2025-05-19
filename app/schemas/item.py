from typing import Optional

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    """Base schema for item data."""
    name: str = Field(..., description="The name of the item")
    description: Optional[str] = Field(None, description="The description of the item")
    price: float = Field(..., description="The price of the item")
    tax: Optional[float] = Field(None, description="The tax rate for the item")


class ItemCreate(ItemBase):
    """Schema for creating a new item."""
    pass


class ItemUpdate(BaseModel):
    """Schema for updating an existing item."""
    name: Optional[str] = Field(None, description="The name of the item")
    description: Optional[str] = Field(None, description="The description of the item")
    price: Optional[float] = Field(None, description="The price of the item")
    tax: Optional[float] = Field(None, description="The tax rate for the item")


class Item(ItemBase):
    """Schema for an item returned from the API."""
    id: int = Field(..., description="The unique identifier of the item")
    
    class Config:
        from_attributes = True
 