############### Working with List #######################

li = [1,4,5,23,546,23,41,333]

s = sorted(li, reverse=True)
print('\nSorted list:\t',s)
################### END ##############################

################## Tuples ############################
tup = (1,4,5,23,546,23,41,333)
# tup.sort() # tuple doesn't have sort function

s_tup = sorted(tup)
print('Sorted Tuples:\t',s_tup)

################### END ##############################


################## Dictionary ########################
di = {'name':'Prashant','job':'programming','age':None,'os':'Linux'}
s_di = sorted(di, reverse=True)       # sort the keys
print('Dict:\t',s_di)

################### END ##############################