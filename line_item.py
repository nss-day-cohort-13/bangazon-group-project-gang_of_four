import uuid


class Line_Item:
''' This will be taking in all of the Line_Item parameters:
    product_uuid and order_uuid

    Also, has the line_item_uuid

    Return: NA
'''

    def __init__(self, product_uuid, order_uuid):
            self.product_uuid = product_uuid
            self.line_item_uuid = uuid.uuid4()
            self.order_uuid = order_uuid

# if __name__ == '__main__':
#   order = Order()