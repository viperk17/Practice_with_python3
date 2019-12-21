import os

# person = {'name' : 'Prashant', 'age':25,'job':'developer'}
# person = {'name' : 'Jess', 'age':22}

# #LBYL ( Non-Pythonic )
# if 'name' in person and 'age' in person and 'job' in person:
#     print("My name is {name}. I am {age} years old and I am a {job}".format(**person))
# else:
#     print("Some keys are missing...")


# #EAFP (Pythonic)
# try:
#     print("I'm {name}. I am {age} years old and I am a {job}".format(**person))
# except KeyError as e:
#     print("Missing {} key".format(e))

# my_list = [1,2,3,4,5,6]
#
# #Non Pythonic
# # if len(my_list) > 6:
# #     print(my_list[5])
# # else:
# #     print('Index does not exist')
#
# #Pythonic
# try:
#     print(my_list[4])
# except IndexError:
#     print('Index does not exist')


#Example from the python docs

my_file = "/home/flyboypk/PycharmProjects/pract/studata.csv"

# #race condition
# if os.access(my_file, os.R_OK):
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print("File could not be found")

#No Race-COndition
try:
    f = open(my_file)
except IOError as e:
    print('File could not be found')
else:
    with f:
        print(f.read())
finally:
    print('Output is above...')
