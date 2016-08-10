import uuid


class Order:
''' This will be taking in all of the order parameters:
       cust_uuid and pay_uuid

    Also, has the order_uuid
      Which will be required by the line_item module

    Return: NA
'''

    def __init__(self, cust_uuid, pay_uuid=None):
            self.cust_uuid = cust_uuid
            self.order_uuid = uuid.uuid4()
            self.order_is_open = True
            self.pay_uuid = pay_uuid

# if __name__ == '__main__':
#   order = Order()