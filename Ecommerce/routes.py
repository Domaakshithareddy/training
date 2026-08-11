from fastapi import APIRouter, status

from schemas import (
    ProductCreate,
    ProductUpdate,
    ProductPatch,
    ApiResponse
)

from service import ProductService

router = APIRouter()

@router.get(
    "/prducts",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK
)
def get_all_products():

    products = ProductService.get_all_products()

    return {
        "success": True,
        "message": "products retrieved successfully.",
        "data": products
    }

@router.get(
    "/products/{product_id}",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK
)
def get_product(product_id: int):

    product = ProductService.get_product_by_id(product_id)

    return {
        "success": True,
        "message": "product retrieved successfully.",
        "data": product
    }

@router.post(
    "/products",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(product: ProductCreate):

    created_product = ProductService.create_product(product)

    return {
        "success": True,
        "message": "product created successfully.",
        "data": created_product
    }

@router.put(
    "/products/{product_id}",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK
)
def update_product(
    product_id: int,
    product: ProductUpdate
):

    updated_product = ProductService.update_product(
        product_id,
        product
    )

    return {
        "success": True,
        "message": "product updated successfully.",
        "data": updated_product
    }

@router.patch(
    "/products/{product_id}",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK
)
def patch_product(
    product_id: int,
    product: ProductPatch
):
    updated_product = ProductService.patch_product(
        product_id,
        product
    )

    return {
        "success": True,
        "message": "product updated successfully.",
        "data": updated_product
    }

@router.delete(
    "/products/{product_id}",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK
)
def delete_product(product_id: int):

    deleted_product = ProductService.delete_product(product_id)

    return {
        "success": True,
        "message": "product deleted successfully.",
        "data": deleted_product
    }