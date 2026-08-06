from typing import Optional,Any
from pydantic import BaseModel,Field

class ProductCreate(BaseModel):
    product_name:str=Field(...,min_length=2,max_length=100)
    category:str=Field(...,min_length=2,max_length=50)
    brand:str=Field(...,min_length=2,max_length=100)
    price:float=Field(...,gt=0)
    stock:int=Field(...,ge=0)

class ProductUpdate(BaseModel):
    product_name:str=Field(...,min_length=2,max_length=100)
    category:str=Field(...,min_length=2,max_length=50)
    brand:str=Field(...,min_length=2,max_length=100)
    price:float=Field(...,gt=0)
    stock:int=Field(...,ge=0)

class ProductPatch(BaseModel):
    product_name:Optional[str]=Field(...,min_length=2,max_length=100)
    category:Optional[str]=Field(...,min_length=2,max_length=50)
    brand:Optional[str]=Field(...,min_length=2,max_length=100)
    price:Optional[float]=Field(...,gt=0)
    stock:Optional[int]=Field(...,ge=0)

class ProductResponse(BaseModel):
    id:int
    product_name:str
    category:str
    brand:str
    price:float
    stock:int

class ApiResponse(BaseModel):
    success:bool
    message:str
    data:Optional[Any]=None