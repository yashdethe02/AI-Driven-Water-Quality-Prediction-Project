from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html

router = APIRouter()

@router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="WaterGuard API Documentation",
        swagger_favicon_url="https://cdn-icons-png.flaticon.com/512/5262/5262027.png",
        swagger_ui_parameters={"defaultModelsExpandDepth": -1}
    )