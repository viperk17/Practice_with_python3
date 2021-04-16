import csv


####################################################################################
# with open('studata.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     with open('new_studata.csv','w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')

#         for line in csv_reader:
#             csv_writer.writerow(line)

## Read the new file with delimeter
# with open('new_studata.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')

#     for line in csv_reader:
#         print(line)


# ''' Using dictionary Reader'''
# with open('studata.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         print(line)
        # print(line['Nationality'])
###########################################################################################

############################# Using Dictionary Writer ####################################

# with open('studata.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with open('dict_studata.csv','w') as new_file:
#         fieldnames = ['Gender','Nationality']
        
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

#         csv_writer.writeheader()

#         for line in csv_reader:
#             csv_writer.writerow(line)


###########################################################################################

# with open('new_sample.csv', 'r') as csv_file:
# with open('studata.csv', 'r') as csv_file:
    # csv_reader = csv.reader(csv_file)
    # print(csv_reader)

    # for line in csv_reader:
    #     print(line)

# ''' Using dictionary Reader'''
# with open('new_sample.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         print(line['policyID'])
        # print(line)
        # next(csv_reader)

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
with open('12.Random.py', 'r') as f:
    # for line in f:
    #     print(line, end='')

    size_to_read = 10
    f_contents = f.read()
#     print(f_contents, end='') 

#     f.seek(3)

#     f_contents = f.read(size_to_read)
#     print(f_contents)

    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')

    while len(f_contents) > 0:
        print(f_contents, end="")      # prints * after every 10 characters
        f_contents = f.read()

###################### END ###############################################################

############################################ Writing With Files ####################################

# # for jpg file use rb or wb
# with open('test.txt','r') as rf:
#     with open('test_copy.txt','w') as wf:
#         for line in rf:
#             wf.write(line)


############################################### END ################################################