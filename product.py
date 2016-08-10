import uuid


class Product:
''' This will be taking in all of the product parameters:
       product_name and product_price

    Also, has the product_uuid
      Which will be required by the line_item module

    Return: NA
'''

    def __init__(self, product_name, product_price):
            self.product_name = product_name
            self.product_price = product_price
            self.product_uuid = uuid.uuid4()

if __name__ == '__main__':
  prod = Product()