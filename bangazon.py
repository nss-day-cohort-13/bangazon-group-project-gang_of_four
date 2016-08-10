import os
import sys
import pickle
import time
import uuid
from customer import *

class Bangazon():

  customers_filename = 'customers.p'
  payments_filename = 'payments.p'
  products_filename = 'products.p'

  def __init__(self):
    """Initialization

    """
    self.current_customer = None

    try:
      self.all_customers = self.deserialize_data(self.customers_filename)
    except EOFError:
      self.all_customers = {}
    try:
      self.all_payments = self.deserialize_data(self.payments_filename)
    except EOFError:
      self.all_payments = {}
    try:
      self.all_products = self.deserialize_data(self.products_filename)
    except EOFError:
      self.all_products = {}

  def page_clear(self):
    """ This clears the page when called

    """
    clear = lambda: os.system('cls')
    clear()

  def show_main_menu(self):
    ''' Shows main menu and allows 'admin' to add products if current user

    '''
    while True:
      self.page_clear()
      if not self.current_customer:
        print('No Current Customer')
      else:
        print('  Current customer: ', self.current_customer.name)
      print("""  *********************************************************
  **  Welcome to Bangazon! Command Line Ordering System  **
  *********************************************************
  1. Create a customer account
  2. Choose active customer
  3. Create a payment option
  4. Add product to shopping cart
  5. Complete an order
  6. See product popularity
  7. Leave Bangazon!""")

      user_choice = input("Select an option: ").lower()
      # time.sleep(1)
      if user_choice == '1':
        self.create_customer()
      elif user_choice == '2':
        self.select_customer()
      elif user_choice == '3':
        self.create_payment_type()
      elif user_choice == '4':
        if not self.current_customer:
          print('Please create or select a customer')
          time.sleep(1.5)
          continue
        else:
          self.open_order()
      elif user_choice == '5':
        if not self.current_customer:
          print('Please create or select a customer')
          time.sleep(1.5)
          continue
        else:
          self.close_order()
      elif user_choice == '6':
        self.run_product_popularity_report()
      elif user_choice == 'admin':
        self.create_product_type()
      elif user_choice == '7':
        sys.exit()
      else:
        print('Invalid Input')
        time.sleep(1)



  def create_customer(self):
    self.page_clear()
    print("Let's create a customer")

    name = input('Enter First and Last Name: ')
    address = input('Enter your Street and House Number: ')
    city = input('Enter your City: ')
    state = input('Enter your State: ')
    postal_code = input('Enter your zip code: ')
    phone_number = input('Enter your phone number: ')
    new_customer = Customer(name, address, city, state, postal_code, phone_number)

    self.current_customer = new_customer
    self.all_customers[new_customer.cust_uuid] = new_customer
    self.serialize_data(self.all_customers, self.customers_filename)
    time.sleep(1)


  def select_customer(self):
    while True:
      self.page_clear()
      print('Select a Customer')
      if self.all_customers == {}:
        print('No customers exist, please create a new customer')
        time.sleep(1.5)
        return #back to main menu
      else:
        cu_line_to_uuid = self.list_customers() # returns uuid {line_number: uuid}
        line_number = input("Select a Customer > ") # line_number = line selected
        if line_number not in cu_line_to_uuid:
          print('Not a valid Customer')
          time.sleep(1)
        else:
          current_uuid = cu_line_to_uuid.get(line_number) # get uuid from cu_line_to_uuid
          self.current_customer = self.all_customers.get(current_uuid) # pass uuid from line = current cust
          return #back to main menu


  def create_payment_type(self):
    self.page_clear()
    print('Create your payment type.')
    time.sleep(.5)
    print('Enter your payment name.')
    payment_name = input('Payment Name: ')
    print('Enter your payment account number.')
    payment_accountNum = input('Payment Account #: ')
    new_payment = Payment(payment_name, payment_accountNum)
    # print('Payment type created.', new_payment.pay_uuid)
    # self.payment = new_payment
    self.all_payments[new_payment.pay_uuid] = new_payment
    self.serialize_data(self.all_payments, 'payments.p')
    time.sleep(1)

  def select_payment_type(self): # will move to within Order Process
    pass

  def create_product_type(self):
    self.page_clear()
    print('Welcome, Admin, to the **Add A Product** Page')
    time.sleep(.5)

    print("\nLet's add a product")
    add_product = input('Enter Product Name: ')
    add_product_price = input('Enter Product Price: ')
    new_product = Product(add_product, add_product_price)
    self.all_products[new_product.product_uuid] = new_product
    print("Your product was created.")
    self.serialize_data(self.all_products, 'products.p')
    time.sleep(5)
    pass

    # user input - product_name, product_price
    # creates product_uuid
    # new_product_type = Product(product_name, product_price, product_uuid)
    pass

  def list_customers(self):
    line_count = 1
    cu_line_to_uuid = {} #new dict to hold uuid
    for uuid, value in self.all_customers.items():
      cu_line_to_uuid[str(line_count)] = uuid
      print('{}.  {}'.format(line_count, value.name))
      line_count += 1
    return cu_line_to_uuid # to select_customer


  def list_payments(self):
    # lists all_payments with a number next to name
    pass

  def list_products(self):
    # lists all_products with a number next to name
    pass


  def open_order(self):
    '''select payment type - select products - save order-id#'''
    self.page_clear()
    print('option 4 - Open Order')
    time.sleep(.5)
    ## called when Add Product is selected
    # new_order = Order(cust_uuid)

    pass

  def close_order(self): # may go on order class
    self.page_clear()
    print('option 5 - Close Order')
    time.sleep(.5)
    pass

  def run_product_popularity_report(self):
    #TBD
    self.page_clear()
    print('option 6 - Report')
    time.sleep(.5)
    pass

  def serialize_data(self, data, filename):
    # wb+ w/r in binday format
    with open(filename, 'wb+') as file:
      pickle.dump(data, file)


  def deserialize_data(self, filename):
    # filename
    # rb+ r/w in binary format
    try:
      with open(filename, 'rb+') as file:
        data = pickle.load(file)
    except FileNotFoundError:
      data = {}
    return data



if __name__ == '__main__':
  bangazon = Bangazon()
  bangazon.show_main_menu()
