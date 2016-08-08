import unittest
from order import *

class TestOrder(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

# ******************* ORDER CREATION ****************************
  def test_new_order_creation(self):
    order = Order(
              user = cust_uuid,
              payment_option = pmt_option_uuid,
              open=True
              )

    #not sure if this is written correctly (below)
    self.assertEqual(order.user_id, cust_uuid)
    self.assertIsInstance(order, Order)
    self.assertIsNotNone(customer.cust_uuid)

if __name__ == '__main__':
  unittest.main()
