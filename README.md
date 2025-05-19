# API Template

A template for creating a structured FastAPI application with a layered architecture.

## Project Structure

```
.
├── app/
│   ├── config/      # Configuration settings
│   ├── utils/       # Utility functions 
│   ├── schemas/     # Pydantic models
│   ├── services/    # Business logic
│   ├── repositories/# Data access
│   └── routes/      # API routes
│       ├── api/     # API router
│       └── v1/      # API version 1
│           └── endpoints/ # API endpoints
├── .env             # Environment variables
└── pyproject.toml   # Project metadata and dependencies
```

## Getting Started

1. Set up the environment using uv:
   ```bash
   # Install uv if not already installed
   pip install uv

   # Create a virtual environment and install dependencies
   uv venv
   uv pip install -e .

   # For development dependencies
   uv pip install -e ".[dev]"
   ```

2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Access the API documentation at http://localhost:8000/docs

## Features

- Structured API with a layered architecture
- Dependency injection
- Environment configuration
- Custom logging
- API versioning
- Comprehensive error handling
- Middleware for request/response logging
- Python packaging with pyproject.toml
- uv package manager for faster dependency resolution

## License

MIT 