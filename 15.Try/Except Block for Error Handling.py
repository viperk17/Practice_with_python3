
try:
    f = open('studata.csv')
    #for currupt file exception
    # if f.name == 'studata.csv':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Something went wrong!')
else:
    print(f.read())
    f.close()
finally:    #finally runs in both cases if exception is there or not
    print('Executing Finally..!!')