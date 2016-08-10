import uuid


class Payment:
''' This will be taking in all of the payment parameters:
      payment_name and payment_accountNum

    Also, has the payement_uuid
      Which will be required by the order_item module

    Return: NA
'''


    def __init__(self, payment_name, payment_accountNum):
            self.payment_name = payment_name
            self.payment_accountNum = payment_accountNum
            self.pay_uuid = uuid.uuid4()


if __name__ == '__main__':
  pay = Payment()
