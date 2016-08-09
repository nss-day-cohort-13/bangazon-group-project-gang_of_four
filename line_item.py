import uuid


class Line_Item:

    '''only passing in 'self' because other than that there is only the uuids
    and the open or close thing'''
    def __init__(self, product_uuid, order_uuid):
            self.product_uuid = product_uuid
            self.line_item_uuid = uuid.uuid4()
            self.order_uuid = order_uuid

# if __name__ == '__main__':
#   order = Order()