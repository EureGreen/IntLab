from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings

from app.middleware.logger import LoggingMiddleware
from app.middleware.rate_limit import RateLimitMiddleware
from app.middleware.error_handler import global_exception_handler

from app.api.routes import router
from app.api.health import router as health_router
from app.api.metrics import router as metrics_router


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

# Middlewares

app.add_middleware(LoggingMiddleware)

app.add_middleware(RateLimitMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000",
        "http://localhost:8000",
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handler

app.add_exception_handler(
    Exception,
    global_exception_handler
)

# API

app.include_router(router)
app.include_router(health_router)
app.include_router(metrics_router)

# Frontend

app.mount(
    "/",
    StaticFiles(directory="frontend", html=True),
    name="frontend"
)