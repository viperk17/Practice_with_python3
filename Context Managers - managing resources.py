# '''we are gonna create a script which will open the file and close it auto'''
# class Open_File():
#
#     #going to accept arguments lso access attri that we set from our other methods
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()
#
# with Open_File('sampl.txt', 'w') as f:
#     f.write('Testing...')
#
# print(f.closed)


# # USING FUNCTIONS
# from contextlib import contextmanager
#
# @contextmanager
# def open_file(file, mode):
#     try:
#         f = open_file(file, mode)
#         yield f
#     finally:
#         f.close()
#
# with open_file('abc.txt', 'w') as f:
#     f.write('Testing using functions!!')
#
# print(f.closed)


# using OS module
import os
from contextlib import contextmanager


# cwd = os.getcwd()
# os.chdir('Sample-Dir_One')
# print(os.listdir())
# os.chdir()
#
# cwd = os.getcwd()
# os.chdir('Sample-Dir_Two')
# print(os.listdir())
# os.chdir()



@contextmanager
def change_dir(destnation):
    try:
        cwd = os.getcwd()
        os.chdir(destnation)
        yield

    finally:
        os.chdir(cwd)


# with change_dir('Practice_with_python3'):
#     print(os.listdir())

with change_dir('PycharmProjects'):
    print(os.listdir())
