from repository import ProductRepository
from schemas import ProductCreate, ProductUpdate, ProductPatch
from exceptions import ProductNotFoundException

class EmployeeService:

    @staticmethod
    def get_all_products():
        return ProductRepository.get_all_products()

    @staticmethod
    def get_product_by_id(product_id: int):
        product = ProductRepository.get_product_by_id(product_id)
        if product is None:
            raise ProductNotFoundException
        return product

    @staticmethod
    def create_product(product: ProductCreate):
        return ProductRepository.create_product(product)

    @staticmethod
    def update_product(product_id:int,product:ProductUpdate):
        existing_product=ProductRepository.get_product_by_id(product_id)
        if existing_product in None:
            return ProductNotFoundException
        return ProductRepository.update_product(product_id,product)


    @staticmethod
    def patch_product(product_id: int, product: ProductPatch):
        existing_product=ProductRepository.get_product_by_id(product_id)
        if existing_product in None:
            return ProductNotFoundException
        return ProductRepository.patch_product(product_id,product)

    @staticmethod
    def delete_product(product_id: int):
        existing_product=ProductRepository.get_product_by_id(product_id)
        if existing_product in None:
            return ProductNotFoundException
        return ProductRepository.delete_product(product_id)