import unittest
from product import *
from payment import *
from line_item import *
from order import *
from customer import *


class TestLineItem(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

# ******************* LINE ITEM ****************************
  def test_new_line_item(self):
    customer = Customer("Billy Bob", "123 Melbourne", "Hville", "VA", "12345", "123-456-7890")
    order = Order(customer.cust_uuid, pay_uuid=None)
    payment = Payment("Goats", "2")
    product = Product("CraftBeer", "6")
    line_item = Line_Item(
              product.product_uuid,
              order.order_uuid
              )

    self.assertEqual(line_item.order_uuid, order.order_uuid)
    self.assertEqual(line_item.product_uuid, product.product_uuid)
    self.assertEqual(order.order_is_open, True)
    self.assertIsInstance(line_item, Line_Item)
    self.assertIsNotNone(line_item.line_item_uuid)
    self.assertIsNotNone(order.order_uuid)
    self.assertIsNotNone(payment.pay_uuid)
    self.assertIsNotNone(customer.cust_uuid)
    self.assertIsNotNone(product.product_uuid)

if __name__ == '__main__':
  unittest.main()
