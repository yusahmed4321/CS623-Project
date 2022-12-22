Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# import Libraries
import psycopg2
import os

psql_pw = os.environ.get('PSQL_AUTH')


def drop_constraint(table_name, constraint_name):
    """Drops constraint of a table by passing table name and constraint name"""
    cur.execute(f'''ALTER TABLE {table_name} DROP CONSTRAINT {constraint_name}; ''')

... 
... # Log in info
... con = psycopg2.connect(
...     host="localhost",
...     database="CS623_Project_ya89495n@pace.edu",
...     user="postgres",
...     password="admin"
... )
... 
... # The database needs to implement ACID properties
... # For isolation: SERIALIZABLE
... con.set_isolation_level(3)
... # For atomicity
... con.autocommit = False
... 
... try:
...     cur = con.cursor()
...     # call function to drop the foreign key
...     drop_constraint("Stock", "fk_stock_product")
... 
...     # create a new constraint specifying the constraint to have ON UPDATE CASCADE ON DELETE CASCADE action
...     cur.execute('''ALTER TABLE Stock ADD CONSTRAINT fk_stock_product FOREIGN KEY(prodId) REFERENCES Product(prodId)
...     ON DELETE CASCADE ON UPDATE CASCADE;''')
... 
...     # Rename p1 to pp1 in the product table
...     cur.execute('''UPDATE Product SET prodId='pp1' WHERE  prodId='p1';''')
... 
...     print('Tables are successfully updated')
... except (Exception, psycopg2.DatabaseError) as err:
...     print(err)
...     print("Transactions not be completed,database will be rolled back")
...     con.rollback()
... finally:
...     if con:
...         con.commit()
...         con.close()
