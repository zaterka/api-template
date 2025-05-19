from typing import Dict, List, Optional

from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.utils.custom_logger import get_custom_logger

logger = get_custom_logger(__name__)


class ItemService:
    """Service for item operations."""
    
    def __init__(self):
        # In-memory database for this example
        self.items: Dict[int, Item] = {}
        self.counter = 0
    
    def get_items(self) -> List[Item]:
        """Get all items."""
        logger.info("Getting all items")
        return list(self.items.values())
    
    def get_item(self, item_id: int) -> Optional[Item]:
        """Get an item by ID."""
        logger.info(f"Getting item with ID: {item_id}")
        return self.items.get(item_id)
    
    def create_item(self, item: ItemCreate) -> Item:
        """Create a new item."""
        logger.info("Creating a new item")
        self.counter += 1
        new_item = Item(id=self.counter, **item.model_dump())
        self.items[self.counter] = new_item
        return new_item
    
    def update_item(self, item_id: int, item: ItemUpdate) -> Optional[Item]:
        """Update an existing item."""
        logger.info(f"Updating item with ID: {item_id}")
        if item_id not in self.items:
            return None
        
        stored_item = self.items[item_id]
        update_data = item.model_dump(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(stored_item, field, value)
        
        self.items[item_id] = stored_item
        return stored_item
    
    def delete_item(self, item_id: int) -> bool:
        """Delete an item."""
        logger.info(f"Deleting item with ID: {item_id}")
        if item_id not in self.items:
            return False
        
        del self.items[item_id]
        return True


# Singleton instance
item_service = ItemService() 