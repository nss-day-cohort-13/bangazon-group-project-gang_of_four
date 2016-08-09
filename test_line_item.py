import unittest
from line_item import *
from order import *
from customer import *


class TestLineItem(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

# ******************* LINE ITEM ****************************
  def test_new_line_item(self):
    order = Order(customer.cust_uuid, payment.pay_uuid)
    line_item = Line_Item(
              product.uuid,
              order_uuid
              )

    #not sure if this is written correctly (below)
    self.assertEqual(line_item.order_uuid, order.order_uuid)
    self.assertEqual(line_item.pay_uuid, None)
    self.assertEqual(line_item.order_is_open, True)
    self.assertIsInstance(line_item, Line_Item)
    self.assertIsNotNone(line_item.cust_uuid)
    self.assertIsNone(line_item.pay_uuid)
    self.assertIsNotNone(line_item.line_item_uuid)

if __name__ == '__main__':
  unittest.main()
