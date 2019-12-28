l1 = ['Bhindi', 'Aloo','Noodles','chopsticks']

# i=1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Please buy (item)")
#     i+=1

#using enum
for index, item in enumerate(l1):
    #for index starting at 1 as by default it starts at zero
    if index % 2 ==0:
        print(f"Please buy {item}")