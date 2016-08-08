import unittest
from payment import *

class TestPayment(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

# ******************* NEW PAYMENT ****************************
  def test_new_payment_creation(self):
    payment = Payment(
              payment_name = "visa",
              payment_accountNum = "123456"
              )


    self.assertEqual(payment.payment_name, "visa")
    self.assertEqual(payment.payment_accountNum, "123456")
    self.assertIsInstance(payment, Payment)
    self.assertIsNotNone(payment.pay_uuid)

if __name__ == '__main__':
  unittest.main()
