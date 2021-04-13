import csv

with open('sample.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)

''' Using dictionary Reader'''
with open('sample.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['policyID'])

    '''to read the file
    for line in csv_reader:
        print(line)
    '''
    # next(csv_reader)

    with open('new_sample.csv', 'w') as ns:
        csv_writer = csv.writer(ns, delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)
    #
