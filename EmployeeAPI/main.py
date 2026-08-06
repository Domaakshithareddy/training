from fastapi import FastAPI
from routes import router
from exceptions import register_exception_handlers

app = FastAPI(
    title="Employee Management API",
    description="Production Ready Employee Management REST API",
    version="1.0.0"
)

register_exception_handlers(app)

app.include_router(
    router,
    prefix="/api/v1",
    tags=["Employees"]
)