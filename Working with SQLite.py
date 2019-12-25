import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')
# conn = sqlite3.connect(':memory:')  #it gives fresh memory run
c = conn.cursor()


# c.execute("""Create Table employees (
#             first text,
#             last text,
#             pay integer
#             )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def gets_emp_by_name(lastname):
    c.execute("select * from employees where last=:last", {'last': 'lastname'})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                        WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


'''
Queries:

insert_emp(emp1)
insert_emp(emp2)

emps = gets_emp_by_name('Prashant')
print(emps)

update_pay(emp2, 20200000)
remove_emp(emp1)
conn.close()
'''

c.execute("INSERT INTO employees VALUES ('Prashant', 'SINGH', 5000)")
c.execute("INSERT INTO employees VALUES ('Arun', 'Sharma', 50050)")
c.execute("INSERT INTO employees VALUES ('Rahul', 'Nambiar', 45000)")

# emp1 = Employee('John', 'Cena', 5145555)

# c.execute("INSERT INTO employees VALUES ('{}', '{}', '{}'".format(emp1.first, emp1.last, emp1.pay))
# vulnearble to sql injectiion attcak, cz its not properly excaped

# We can instead use this : its going to be a tupple, #other way to use placeholders properly
# its going to be dict instead tuple
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
#           {'first':emp1.first, 'last':emp1.last, 'pay':emp1.pay})


# c.execute("select * from employees where last='Sharma'")

# or use the below on with employee module
# c.execute("select * from employees where last=?", ('Singh',))   #, will make it tuple or else it wll give error
# or using dict
# c.execute("select * from employees where last=:last", {'last':'Singh'})

emps = gets_emp_by_name('SINGH')
print(emps)

# print(c.fetchone())
# print(c.fetchmany())
# print(c.fetchall())

conn.commit()
conn.close()
