import unittest
from product import *


class TestCustomer(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

# ******************* NEW Product ****************************
  def test_new_product_creation(self):
    product = Product(
              product_name = "craft beer",
              product_price = "$6"
              )


    self.assertEqual(product.product_name, "craft beer")
    self.assertEqual(product.product_price, "$6")
    self.assertIsInstance(product, Product)
    self.assertIsNotNone(product.product_uuid)

if __name__ == '__main__':
  unittest.main()

