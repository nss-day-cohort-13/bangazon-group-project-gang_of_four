import unittest
from bangazon import *

class TestBangazon(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.bangazon = Bangazon()
    pass
# ******************* Test Serialize ****************************

  def test_serialize_data(self):
    serial_test = 'cereal'

    self.bangazon.serialize_data(serial_test, 'test.p')
    test1 = self.bangazon.deserialize_data('test.p')

    self.assertEqual(serial_test, test1)



if __name__ == '__main__':
  unittest.main()
