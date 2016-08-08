import uuid


class Payment:


    def __init__(self, payment_name, payment_accountNum):
            self.payment_name = payment_name
            self.payment_accountNum = payment_accountNum
            self.pay_uuid = uuid.uuid4()


if __name__ == '__main__':
  pay = Payment()
