import logging
from typing import Optional

from app.config.settings import get_settings

settings = get_settings()


def get_custom_logger(name: str, level: Optional[str] = None) -> logging.Logger:
    """
    Get a custom logger with a specific name and level.
    
    Args:
        name: The name of the logger.
        level: The log level. If None, it will use the level from settings.
        
    Returns:
        A configured logger instance.
    """
    logger = logging.getLogger(name)
    
    # Set log level from settings if not provided
    log_level = level or settings.LOG_LEVEL
    logger.setLevel(logging.getLevelName(log_level))
    
    # Create a console handler if it doesn't exist
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.getLevelName(log_level))
        
        # Create a formatter with timestamp
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(formatter)
        
        # Add the handler to the logger
        logger.addHandler(console_handler)
    
    return logger 