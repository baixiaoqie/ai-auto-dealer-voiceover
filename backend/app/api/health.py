from fastapi import APIRouter
from pydantic import BaseModel
from ..core import logger

router = APIRouter()


class HealthResponse(BaseModel):
    """健康检查响应"""
    status: str
    message: str


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """健康检查接口"""
    logger.debug("健康检查被调用")
    return HealthResponse(
        status="ok",
        message="服务运行正常"
    )
