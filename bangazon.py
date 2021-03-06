import os
import sys
import pickle
import time
import uuid
from customer import *
from payment import *
from product import *
from table import *
from order import *
from line_item import *

class Bangazon():

  customers_filename = 'bangazon.db'
  payments_filename = 'payments.p'
  products_filename = 'products.p'
  orders_filename = 'orders.p'
  line_items_filename = 'line_items.p'

  def __init__(self):
    """Initialization

    """
    self.current_customer = None
    self.current_product = None
    self.current_payment = None
    self.current_order = None
    self.current_line_items = None
    self.all_payments = None



    self.all_customers = BangTable.query_all_customers()
    self.all_payments = BangTable.query_all_payments()
    self.all_products = BangTable.query_all_products()
    # try:
    #   self.all_customers = self.deserialize_data(self.payments_filename)
    # except EOFError:
    #   self.all_customers = {}
    # try:
    #   self.all_payments = self.deserialize_data(self.payments_filename)
    # except EOFError:
    #   self.all_payments = {}
    # try:
    #   self.all_products = self.deserialize_data(self.products_filename)
    # except EOFError:
    #   self.all_products = {}
    try:
      self.all_orders = self.deserialize_data(self.orders_filename)
    except EOFError:
      self.all_orders = {}

      self.all_line_items = self.deserialize_data(self.line_items_filename)
    except EOFError:
      self.all_line_items = {}

  def page_clear(self):
    """ This clears the page when called

    """
    os.system('cls' if os.name == 'nt' else 'clear')

  def show_main_menu(self):
    ''' Shows main menu and allows 'admin' to add products if current user

    '''
    while True:
      self.page_clear()
      if not self.current_customer:
        print('No Current Customer')

      else:
        print('Current customer: ', self.current_customer[1])
        # print('Current apyment: ', self.current_payment[1])
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
          self.select_product_type()
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
      elif user_choice == 'customers':
        self.list_customers()
        time.sleep(4)
      elif user_choice == 'payments':
        if not self.all_payments:
          print('No payments types exist')
          time.sleep(1.5)
          continue
        else:
          self.list_payments()
          time.sleep(4)
      elif user_choice == 'products':
        self.list_products()
        time.sleep(4)
      elif user_choice == 'orders':
        self.list_orders()
        time.sleep(4)
      elif user_choice == 'line items':
        self.list_orders()
        time.sleep(4)
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
    new_customer = (None, name, address, city, state, postal_code, phone_number)

    self.current_customer = BangTable.customer_table(new_customer)
    self.all_customers.append(self.current_customer)
    time.sleep(1)
    # BangTable.create_customer(new_customer)


  def select_customer(self):
    while True:
      self.page_clear()
      print('Select a Customer')
      if self.all_customers == []:
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
          self.current_customer = self.all_customers[int(line_number) - 1] # pass uuid from line = current cust
          return #back to main menu


  def create_payment_type(self):
    self.page_clear()
    print('Create your payment type.')
    time.sleep(.5)
    print('Enter your payment name.')
    payment_name = input('Payment Name: ')
    print('Enter your payment type.')
    payment_account_number = input('Payment Method: ')
    new_payment = (None, payment_name, payment_account_number)

    self.current_payment = BangTable.payment_table(new_payment)
    self.all_payments.append(self.current_payment)
    time.sleep(1)


  def select_payment_type(self): # will move to within Order Process
    while True:
      self.page_clear()
      print('Select a Payment')
      if self.all_payments == {}:
        print('No payments exist')
        time.sleep(1.5)
        return #back to main menu
      else:
        pa_line_to_uuid = self.list_payments() # returns uuid {line_number: uuid}
        line_number = input("Select a Payment > ") # line_number = line selected
        if line_number not in pa_line_to_uuid:
          print('Not a valid Payment')
          time.sleep(1)
        else:
          self.current_payment = self.all_payments[int(line_number) - 1] # pass uuid from line = current payment
          print('Payment type is: ', self.current_payment)
          return #back to main menu


  def create_product_type(self):
    self.page_clear()
    print('Welcome to the **Add A Product** Page')
    time.sleep(1)

    print("\nLet's add a product")
    add_product = input('Enter Product Name: ')
    add_product_price = input('Enter Product Price $ ')
    new_product = (None, add_product, add_product_price)

    self.current_product = BangTable.product_table(new_product)
    self.all_products.append(self.current_product) # pass in new_product to all_products)
    # self.all_products.append(self.new_product) # use this instead if don't care about current product
    time.sleep(2)
    pass

  def select_product_type(self):
    while True:
      self.page_clear()
      print('Select a Product')
      if self.all_products == {}:
        print('No products exist')
        time.sleep(1.5)
        return #back to main menu
      else:
        pr_line_to_uuid = self.list_products() # returns uuid {line_number: uuid}
        line_number = input("Select a Product > ") # line_number = line selected
        if line_number not in pr_line_to_uuid:
          print('Not a valid Product')
          time.sleep(1)
        else:

    # current_uuid = pr_line_to_uuid.get(line_number) # get uuid from pr_line_to_uuid
          self.current_product = self.all_products[int(line_number) -1] # pass uuid from line = current product
          #current_uuid = product_uuid this is what we need to push to line_item after order has been created
          # product_uuid = current_uuid
          print('You chose: ', self.current_product)
          # print('current cust', self.current_customer.cust_uuid)
          # print(product_uuid)
          time.sleep(1.5)
#program crashes here - need to split off Order and then New Line Item
          new_order = Order(self.current_customer.cust_uuid)
          self.all_orders[new_order.order_uuid] = new_order
          BangTable.order_table(new_order)
          print(new_order.order_uuid)
          time.sleep(1)


          new_line_item = Line_Item(product_uuid, new_order.order_uuid)

          return #back to main menu

  def list_customers(self):
    line_count = 1
    cu_line_to_uuid = {} #new dict to hold uuid
    for value in self.all_customers:
      cu_line_to_uuid[str(line_count)] = value[0]
      print('{}.  {}'.format(line_count, value[1]))
      line_count += 1
    return cu_line_to_uuid # to select_customer


  def list_payments(self):
    line_count = 1
    pa_line_to_uuid = {} #new dict to hold uuid
    for value in self.all_payments:
      pa_line_to_uuid[str(line_count)] = value[0]
      print('{}.  {}'.format(line_count, value[1]))
      line_count += 1
    return pa_line_to_uuid # to select_payment

  def list_products(self):
    line_count = 1
    pr_line_to_uuid = {} #new dict to hold uuid
    for value in self.all_products:
      pr_line_to_uuid[str(line_count)] = value[0]
      print('{}.  {}'.format(line_count, value[1]))
      line_count += 1
    return pr_line_to_uuid # to select_product

  def list_orders(self):
    line_count = 1
    or_line_to_uuid = {} #new dict to hold uuid
    for value in self.all_orders:
      or_line_to_uuid[str(line_count)] = value[0]
      print('{}.  Order UUID {}'.format(line_count, value[1]))
      line_count += 1
    return or_line_to_uuid # to select_product

  def list_line_item(self):
    line_count = 1
    li_line_to_uuid = {} #new dict to hold uuid
    for value in self.all_orders:
      li_line_to_uuid[str(line_count)] = value[0]
      print('{}.  Order UUID {}'.format(line_count, value[1]))
      line_count += 1
    return li_line_to_uuid # to select_product


  def open_order(self):
    '''select payment type - select products - save order-id#'''
    self.page_clear()
    print('option 4 - Open Order')
    time.sleep(.5)
    ## called when Add Product is selected
    # new_order = Order(cust_uuid)

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
