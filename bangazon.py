import os
import sys
import pickle
import time # if we need time
import uuid
from customer import *

class Bangazon():

  def __init__(self):
    """Initialization

    """
    self.current_customer = None


    try:
      self.all_customers = self.deserialize_customers()
    except EOFError:
      self.all_customers = {}
    try:
      self.all_payments = self.deserialize_payments()
    except EOFError:
      self.all_payments = {}
    try:
      self.all_products = self.deserialize_products()
    except EOFError:
      self.all_products = {}

  def page_clear(self):
    """ This clears the page when called

    """
    clear = lambda: os.system('cls')
    clear()

  def show_main_menu(self):
    # shows main menu and allows 'admin' to add products if current user
    while True:
      self.page_clear()

      print('  Current customer: ', self.current_customer)
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
      print('x', user_choice)
      time.sleep(1)
    # if user_choice in 'option':
      if user_choice == '1':
        self.create_customer()
      elif user_choice == '2':
        self.select_customer()
      elif user_choice == '3':
        self.create_payment_type()
      elif user_choice == '4':
        self.open_order()
      elif user_choice == '5':
        self.close_order()
      elif user_choice == '6':
        self.run_product_popularity_report()
      elif user_choice == 'admin':
        self.create_product_type()
      elif user_choice == '7':
        sys.exit
      else:
        return self.show_main_menu()



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
    print('test creation', new_customer.cust_uuid)
    self.current_customer = new_customer
    print('current cust', self.current_customer.name)
    time.sleep(1)
    pass

  def select_customer(self):
    self.page_clear()
    print('option 2 Select Customer')
    time.sleep(.5)
    # allows selection of customer
    # makes current_customer = selected_customer
    pass

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
    self.all_customers[new_customer.cust_uuid] = new_customer
    self.serialize_data(self., 'customers.p')
    time.sleep(1)
    self.show_main_menu()
    time.sleep(.5)
    # user input - payment_name, payment_accountNum
    # creates pay_uuid
    # new_payment_type = Payment(payment_name, payment_accountNum, pay_uuid)
    pass

  def select_payment_type(self): # will move to within Order Process
    pass

  def create_product_type(self):
    self.page_clear()
    print('Welcome Admin')
    time.sleep(.5)
    # user input - product_name, product_price
    # creates product_uuid
    # new_product_type = Product(product_name, product_price, product_uuid)
    pass

  def list_customers(self):
    # lists all_customers with a number next to name
    pass

  def list_payments(self):
    # lists all_payments with a number next to name
    pass

  def list_products(self):
    # lists all_products with a number next to name
    pass

  def open_order(self):
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

  def serialize_customers(self):
    # wb+ w/r in binday format
    pass

  def deserialize_customers(self):
    # rb+ r/w in binary format
    pass

  def serialize_payments(self):
    # wb+ w/r in binday format
    pass

  def deserialize_payments(self):
    # rb+ r/w in binary format
    pass

  def serialize_products(self):
    # wb+ w/r in binday format
    pass

  def deserialize_products(self):
    # rb+ r/w in binary format
    pass


if __name__ == '__main__':
  bangazon = Bangazon()
  bangazon.show_main_menu()
