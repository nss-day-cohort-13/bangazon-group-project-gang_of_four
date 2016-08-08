import uuid


class Customer:


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