import uuid


class Order:

    '''only passing in 'self' because other than that there is only the uuids
    and the open or close thing'''
    def __init__(self, cust_uuid, pay_uuid=None):
            self.cust_uuid = cust_uuid
            self.order_uuid = uuid.uuid4()
            self.order.open = True
            self.pay_uuid = pay_uuid

if __name__ == '__main__':
  o = Order()