from fastapi import APIRouter

from app.services.metrics_service import MetricsService


router = APIRouter(
    prefix="/api",
    tags=["Metrics"]
)


service = MetricsService()


@router.get("/metrics")
async def metrics():

    return service.get_metrics()