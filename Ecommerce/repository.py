from schemas import ProductCreate,ProductPatch,ProductUpdate

products=[]
next_product_id=1

class ProductRepository:

    @staticmethod
    def get_all_products():
        return products

    @staticmethod
    def get_product_by_id(product_id:int):
        for product in products:
            if product["id"]==product_id:
                return product
        return None

    @staticmethod
    def create_product(product:ProductCreate):
        global next_product_id
        product_data={
            'id':next_product_id,
            'product_name':product.product_name,
            'category':product.category,
            'brand':product.brand,
            'pricee':product.price,
            'stock':product.stock
        }
        products.append(product_data)
        next_product_id+=1
        return product_data

    @staticmethod
    def update_product(product_id:int,product):
        for index,prod in enumerate(products):
            if prod['id']==index:
                updated_prod={
                    'id':product_id,
                    'product_name':product.product_name,
                    'category':product.category,
                    'brand':product.brand,
                    'pricee':product.price,
                    'stock':product.stock
                }
                products[index]=updated_prod
                return updated_prod

    @staticmethod
    def patch_product(product_id:int,product):
        for ext_product in products:
            if ext_product['id']==product_id:
                if product.product_name is not None:
                    ext_product['product_name']=product.product_name
                if product.category is not None:
                    ext_product['category']=product.category
                if product.brand is not None:
                    ext_product['brand']=product.brand
                if product.price is not None:
                    ext_product['price']=product.price
                if product.stock is not None:
                    ext_product['stock']=product.stock
                return ext_product
        return None

    @staticmethod
    def delete_product(product_id:int):
        for idx,prod in enumerate(products):
            if prod['id']==product_id:
                return products.pop(idx)
        return None