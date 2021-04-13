from collections import namedtuple

'''SQL DB Connection'''
# import sqlite3
# conn = sqlite3.connect('employee.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE employees (
# first text,
# last text,
# pay integer
# """)
# conn.commit()
# conn.close()

dict_color = {'red': 55, 'green': 155, 'blue': 255}
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 125, 255)
# white = Color(255,255,255)
print(color.red)
