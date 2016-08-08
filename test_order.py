import unittest
from order import *
from customer import *


class TestOrder(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

# ******************* ORDER CREATION ****************************
  def test_new_order_creation(self):
    customer = Customer("Billy Bob", "123 Melbourne", "Hville", "VA", "12345", "123-456-7890")
    order = Order(
              customer = customer.cust_uuid,
              open=True
              )

    #not sure if this is written correctly (below)
    self.assertEqual(order.cust_uuid, customer.cust_uuid)
    self.assertEqual(order.pay_option_uuid, None)
    self.assertEqual(order.open, True)
    self.assertIsInstance(order, Order)
    self.assertIsNotNone(order.cust_uuid)
    self.assertIsNotNone(order.pay_uuid)
    self.assertIsNotNone(order.order_uuid)

if __name__ == '__main__':
  unittest.main()
