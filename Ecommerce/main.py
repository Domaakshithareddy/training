from fastapi import FastAPI
from routes import router
from exceptions import register_exception_handlers

app=FastAPI(
    title='Ecommerce application',
    description='Retail ecommerce application',
    version='1.0.0'
)

register_exception_handlers(app)

app.include_router(
    router,
    prefix='/app/e1',
    tags=['Ecommerce']
)