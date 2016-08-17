import sys
import sqlite3
from datetime import datetime

class BangTable:
  '''create class for customer table'''

  def customer_table(new_customer):
    '''Puts Customer Data in a Table
    '''
    with sqlite3.connect('bangazon.db') as khan:
      k = khan.cursor()

      try:
        k.execute("""create table customer
          (name text, address text, city text, state text, postal_code text, phone_number text)""")
      except sqlite3.OperationalError:
        pass


      k.execute("insert into customer values (?, ?, ?, ?, ?, ?)",
                    (new_customer.name, new_customer.address, new_customer.city, new_customer.state, new_customer.postal_code, new_customer.phone_number))

      khan.commit()


  def payment_table(new_payment):
    '''Puts Customer Data in a Table
    '''
    with sqlite3.connect('bangazon.db') as khan:
      k = khan.cursor()

      try:
        k.execute("""create table payment
          (payment_name, payment_account_number)""")
      except sqlite3.OperationalError:
        pass


      k.execute("insert into payment values (?, ?)",
                    (new_payment.payment_name, new_payment.payment_account_number))


      khan.commit()
