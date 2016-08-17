import uuid


class Payment:


    def __init__(self, payment_name, payment_account_number):
            self.payment_name = payment_name
            self.payment_account_number = payment_account_number
            self.pay_uuid = uuid.uuid4()


if __name__ == '__main__':
  pay = Payment()
