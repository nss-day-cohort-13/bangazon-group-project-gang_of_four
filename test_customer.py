import unittest



class TestCustomer(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

# ******************* NEW USER ****************************
def test_new_customer_creation(self):
  customer = Customer(
            name = "Customer Name",
            address = "123 Street Name Dr",
            city = "Millville",
            state = "VA",
            postal_code = "12345",
            phone_number = "123-456-7890"
            )


self.assertEqual(customer.name, "Brady Robertson")
self.assertEqual(customer.address, "123 Street Name Dr")
self.assertEqual(customer.city, "Millville")
self.assertEqual(customer.state, "VA")
self.assertEqual(customer.postal_code, "12345")
self.assertEqual(customer.phone_number, "123-456-7890")
self.assertIsInstance(customer, Customer)
self.assertIsNotNone(customer.customer_id) #Not sure what this is for

if __name__ == '__main__':
  unittest.main()

