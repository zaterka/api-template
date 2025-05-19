import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import get_settings
from app.routes import api
from app.utils.custom_logger import get_custom_logger

settings = get_settings()

# Use custom logger instead of the root logger
logger = get_custom_logger(__name__)

# Configure root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for startup and shutdown."""
    logger.info("Application startup: initializing")
    # Initialize any clients or connections here
    logger.info("Application startup: initialization complete")
    
    yield
    
    # Cleanup on shutdown
    logger.info("Application shutdown")


app = FastAPI(
    title="API Template",
    description="Layered API structure template",
    version="0.1.0",
    lifespan=lifespan
)


@app.middleware("http")
async def log_request_response(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    
    response = await call_next(request)
    
    logger.info(f"Response status code: {response.status_code}")
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.endpoint_router)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000) 