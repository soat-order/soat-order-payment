from fastapi import APIRouter
from src.adapter.spi.api.router.health_check_router import router as HealthCheck
from src.adapter.spi.api.router.payment_router import router as PaymentRouter


api_router = APIRouter()
api_router.include_router(HealthCheck, prefix='/health', tags=["healthCheck"])
api_router.include_router(PaymentRouter, prefix='/payments', tags=["payments"])
