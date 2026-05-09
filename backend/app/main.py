from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from .core import settings, logger, engine, Base
from .api import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"{settings.PROJECT_NAME} v{settings.PROJECT_VERSION} starting")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created")
    yield
    logger.info("Application shutdown")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="AI智能口播系统 - 第一阶段：抖音文案解析与改写",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"code": 500, "message": "Internal server error", "data": None},
    )


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(health.router, prefix="/api/v1", tags=["健康检查"])


@app.get("/")
async def root():
    return {
        "message": f"欢迎使用 {settings.PROJECT_NAME}",
        "version": settings.PROJECT_VERSION,
        "docs": "/docs",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
