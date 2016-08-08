import uuid


class Product:


    def __init__(self, product_name, product_price):
            self.product_name = product_name
            self.product_price = product_price
            self.product_uuid = uuid.uuid4()

if __name__ == '__main__':
  prod = Product()