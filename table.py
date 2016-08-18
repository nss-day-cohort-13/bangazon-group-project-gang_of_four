import sys
import sqlite3
from datetime import datetime
import time

class BangTable:
  '''create class for customer table'''

  def customer_table(new_customer):
    '''Puts Customer Data in a Table
    '''
    with sqlite3.connect('bangazon.db') as khan:
      k = khan.cursor()
      try:
        k.execute("""create table customer
          (cust_uuid INTEGER PRIMARY KEY AUTOINCREMENT, name text, address text, city text, state text, postal_code text, phone_number text)""")
      except sqlite3.OperationalError:
        pass
      k.execute("insert into customer values (?, ?, ?, ?, ?, ?, ?)",
                    (None, new_customer.name, new_customer.address, new_customer.city, new_customer.state, new_customer.postal_code, new_customer.phone_number))
      khan.commit()

      print("new_customer.name", new_customer.name)
      new_customer = k.execute("select cust_uuid from customer where name = ?", (new_customer.name,))
      active_customer = new_customer.fetchone()
      print(active_customer)
      time.sleep(5)

  def payment_table(new_payment):
    '''
    Puts Payment Data in Table
    '''
    with sqlite3.connect('bangazon.db') as khan:
      k = khan.cursor()
      try:
        k.execute("""create table payment
          (payment_uuid INTEGER PRIMARY KEY AUTOINCREMENT, payment_name text, payment_account_number text)""")
      except sqlite3.OperationalError:
        pass
      k.execute("insert into payment values (?, ?, ?)",
                    (None, new_payment.payment_name, new_payment.payment_account_number))
      khan.commit()

      print("new_payment.name", new_payment.payment_name)
      new_payment = k.execute("select payment_uuid from payment where payment_name = ?", (new_payment.payment_name,))
      active_payment = new_payment.fetchone()
      print("here is your active payment", active_payment)
      time.sleep(2)

  def product_table(new_product):
      '''
      Puts Product Data in Table
      '''
      with sqlite3.connect('bangazon.db') as khan:
        k = khan.cursor()
        try:
          k.execute("""create table product
            (product_uuid INTEGER PRIMARY KEY AUTOINCREMENT, product_name text, product_price int)""")
        except sqlite3.OperationalError:
          pass
        k.execute("insert into product values (?, ?, ?)",
                      (None, new_product.product_name, new_product.product_price))
        khan.commit()


  def order_table(new_order):
      '''
      Puts Order Data in Table
      '''
      with sqlite3.connect('bangazon.db') as khan:
        k = khan.cursor()
        try:
          k.execute("""create table orders
            (order_uuid INTEGER PRIMARY KEY AUTOINCREMENT, cust_uuid int, pay_uuid int, order_is_open int)""")
        except sqlite3.OperationalError:
          pass

        print(new_order.cust_uuid)
        k.execute("insert into orders (cust_uuid, pay_uuid, order_is_open) values (?, ?, ?)",
                      (new_order.cust_uuid, new_order.pay_uuid, new_order.order_is_open))
        khan.commit()


  def line_item(new_line_item):
      '''
      Puts Line Item Data in Table
      '''
      with sqlite3.connect('bangazon.db') as khan:
        k = khan.cursor()
        try:
          k.execute("""create table order
            (line_item_uuid INTEGER PRIMARY KEY AUTOINCREMENT, new_line_item.order_uuid int, new_line_item.product_uuid int)""")
        except sqlite3.OperationalError:
          pass
        k.execute("insert into order values (?, ?, ?)",
                      (None, new_order.order_uuid, new_order.product_uuid))
        khan.commit()
