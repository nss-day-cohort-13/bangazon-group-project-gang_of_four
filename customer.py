import uuid


class Customer:
''' This will be taking in all of the customer parameters:
    name, address, city, state, postal_code, phone_number

    Also, has the cust_uuid
      Which will be required by the order module

    Return: NA
'''


    def __init__(self, name, address, city, state, postal_code, phone_number):
            self.name = name
            self.address = address
            self.city = city
            self.state = state
            self.postal_code = postal_code
            self.phone_number = phone_number
            self.cust_uuid = uuid.uuid4()

if __name__ == '__main__':
  c = Customer()
