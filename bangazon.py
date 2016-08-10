# ******************** IMPORTS *****************************
import os
import sys
import pickle
import time
import uuid
from customer import *
from payment import *
from product import *

# ******************** MAIN BANGAZON CLASS ********************
class Bangazon():

  customers_filename = 'customers.p'
  payments_filename = 'payments.p'
  products_filename = 'products.p'

  def __init__(self):
    """
    Initialization

    """
    self.current_customer = None
    self.current_product = None
    self.current_payment = None

# ******************** DESERIALIZATION ********************

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

# ******************** CLEARING THE PAGE ********************

  def page_clear(self):
    """
    This clears the page when called

    """
    clear = lambda: os.system('cls')
    clear()


# ******************** SHOWING THE MAIN MENU ********************


  def show_main_menu(self):
    '''
    while True loop that runs through the menu while the program is active

    Shows main menu and allows 'admin' to add products if current user

    '''
    while True:
      self.page_clear()
      if not self.current_customer:
        print('\nNo Current Customer')
      else:
        print('  \nCurrent customer: ', self.current_customer.name)
      print("""  \n*********************************************************
  **  Welcome to Bangazon! Command Line Ordering System  **
  *********************************************************
  \n1. Create a customer account
  2. Choose active customer
  3. Create a payment option
  4. Add product to shopping cart
  5. Complete an order
  6. See product popularity
  7. Leave Bangazon!""")


# else if statements that run through functions needed for menu

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
      else:
        print('Invalid Input')
        time.sleep(1)

# ******************** CREATING CUSTOMER ********************


  def create_customer(self):
    '''
    takes in the inputs and assigns them to variables for customer attributes

    assigns uuid and and serializes data
    '''
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

# ******************** SELECTING CUSTOMER ********************

  def select_customer(self):
    '''
    prints customer list
      goes through exception of no customer yet existing
        and not a valid customer chosen

    gets the uuid for the customer

    assigns uuid
    '''

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

# ******************** CREATING PAYMENT ********************


  def create_payment_type(self):
    '''
    prompts user to create  payment
    asks for payment account number

    assigns uuid and and serializes data
    '''

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

# ******************** SELECTING PAYMENT ********************


  def select_payment_type(self): # will move to within Order Process
    '''
    prints payment options
      goes through exception of payment not existing
      and not a valid payment selected

    gets the uuid for the payment

    '''
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
          current_uuid = pa_line_to_uuid.get(line_number) # get uuid from cu_line_to_uuid
          self.current_payment = self.all_payments.get(current_uuid) # pass uuid from line = current payment
          print('You chose: ', self.all_payments[current_uuid].payment_name)
          time.sleep(1.5)

          return #back to main menu

# ******************** CREATING PRODUCT ********************


  def create_product_type(self):
    '''
    This is the Admin log in page for a product.
    prompts user to product name and price and assigns that to a variable

    serializes data
    '''
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

# ******************** SELECTING  PRODUCT ********************

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

          current_uuid = pr_line_to_uuid.get(line_number) # get uuid from pr_line_to_uuid
          self.current_product = self.all_products.get(current_uuid) # pass uuid from line = current product
          #current_uuid = product_uuid this is what we need to push to line_item after order has been created
          print('You chose: ', self.all_products[current_uuid].product_name)
          time.sleep(1.5)
          return #back to main menu

# ******************** LISTING CUSTOMERS ********************


  def list_customers(self):
    line_count = 1
    cu_line_to_uuid = {} #new dict to hold uuid
    for uuid, value in self.all_customers.items():
      cu_line_to_uuid[str(line_count)] = uuid
      print('{}.  {}'.format(line_count, value.name))
      line_count += 1
    return cu_line_to_uuid # to select_customer

# ******************** LISTING PAYMENTS ********************


  def list_payments(self):
    line_count = 1
    pa_line_to_uuid = {} #new dict to hold uuid
    for uuid, value in self.all_payments.items():
      pa_line_to_uuid[str(line_count)] = uuid
      print('{}.  {}'.format(line_count, value.payment_name))
      line_count += 1
    return pa_line_to_uuid # to select_payment

# ******************** LISTING PRODUCTS ********************

  def list_products(self):
    line_count = 1
    pr_line_to_uuid = {} #new dict to hold uuid
    for uuid, value in self.all_products.items():
      pr_line_to_uuid[str(line_count)] = uuid
      print('{}.  {}'.format(line_count, value.product_name))
      line_count += 1
    return pr_line_to_uuid # to select_product

# ******************** OPEN ORDER ********************


  def open_order(self): #basically = select product type
    pass

# ******************** CLOSE ORDER ********************


  def close_order(self): # may go on order class
    self.page_clear()
    print('option 5 - Close Order')
    time.sleep(.5)
    pass

# ******************** POPULARITY REPORT ********************

  def run_product_popularity_report(self):
    #TBD
    self.page_clear()
    print('option 6 - Report')
    time.sleep(.5)
    pass

# ******************** SERIALIZE DATA ********************

  def serialize_data(self, data, filename):
    # wb+ w/r in binday format
    with open(filename, 'wb+') as file:
      pickle.dump(data, file)

# ******************** DESERIALIZE DATA ********************


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
