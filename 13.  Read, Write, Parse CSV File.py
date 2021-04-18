# import csv

# with open('sample.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     print(csv_reader)

# ''' Using dictionary Reader'''
# with open('sample.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         print(line['policyID'])

#     '''to read the file
#     for line in csv_reader:
#         print(line)
#     '''
#     # next(csv_reader)

#     with open('new_sample.csv', 'w') as ns:
#         csv_writer = csv.writer(ns, delimiter='\t')
#         for line in csv_reader:
#             csv_writer.writerow(line)
#     

################ Reading file contents ###################################################
# with open('12.Random.py', 'r') as f:
#     # for line in f:
#     #     print(line, end='')

#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='') 

#     f.seek(3)

#     f_contents = f.read(size_to_read)
#     print(f_contents)

    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')

    # while len(f_contents) > 0:
    #     print(f_contents, end="*")      # prints * after every 10 characters
    #     f_contents = f.read(size_to_read)

###################### END ###############################################################

############################################ Writing With Files ####################################

# # for jpg file use rb or wb
# with open('test.txt','r') as rf:
#     with open('test_copy.txt','w') as wf:
#         for line in rf:
#             wf.write(line)


############################################### END ################################################
