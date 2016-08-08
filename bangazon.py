import os
import sys
import pickle
import time # if we need time
import uuid

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
    # clears page when called
    pass

  def show_main_menu(self):
    # shows main menu and allows 'admin' to add products if current user
    pass

  def create_customer(self):
    # user input - name, address, city, state, postal_code, phone_number
    # creates cust_uuid
    # new_customer = Customer(name, address, city, state, postal_code, phone_number, cust_uuid)
    pass

  def select_customer(self):
    # allows selection of customer
    # makes current_customer = selected_customer
    pass

  def create_payment_type(self):
    # user input - payment_name, payment_accountNum
    # creates pay_uuid
    # new_payment_type = Payment(payment_name, payment_accountNum, pay_uuid)
    pass

  def select_payment_type(self): # will move to within Order Process
    pass

  def create_product_type(self):
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
    ## called when Add Product is selected
    # new_order = Order(cust_uuid)
    pass

  def close_order(self): # may go on order class
    pass

  def run_product_popularity_report(self):
    #TBD
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
  bandgazon.show_main_menu()