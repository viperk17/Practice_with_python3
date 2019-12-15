# f = open('10. Modules.py', 'r')
# with open('10. Modules.py','r') as f:
#     pass

#
# with open('10. Modules.py','r') as f:
#
#     # for line in f:
#     #     print(line, end='')
#
#     f_contents = f.read(10)  #read all data
#     print(f_contents, end = '\n@')
#
#     print(f.tell())
#
#     f.seek(0)
#     f_contents = f.read(10)  # read all data
#     print(f_contents, end='@')


#2 Create file
# with open('test.txt', 'r') as m:    #create a file in write mode
#     with open('test1.txt', 'w') as wf:
#         for line in m:
#             wf.write(line)
    # m.write('I am the King')
    # m.close()


# chunk file size
with open('test.txt', 'r') as m:    #create a file in write mode
    with open('test1.txt', 'w') as wf:
        chunk_size = 4096
        m_chunk = m.read(chunk_size)


# # print(f.mode)
# # f.close()
#     f_contents = f.readline() #reads line
#     print(f_contents, end='')