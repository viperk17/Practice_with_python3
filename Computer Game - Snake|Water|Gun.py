import random

list1 = ['s', 'w', 'g']

chance = 5
no_of_chances = 0
comp_points = 0
user_points = 0

print("\t\t Snake | Water | Gun Game with Computer\n")
print("\t\t S for Snake | W for Water | G for Gun \n")

# validations
while no_of_chances < chance:
    # print("\t\tMake a selection...")
    ip = input('\t\tSnake, Water, Gun : \n')
    random_ = random.choice(list1)

    if ip.lower() == random_:
        print("It's a tie...")
        print(f"Your guess {ip} and Computer guess is {ip}")


    # if input s
    elif ip.lower() == 's' and random == 'g':
        comp_points += 1
        print(f"Your guess {ip} and Computer guess is {ip}")
        print('Comp wins 1 point')
        print(f"Comp points are {comp_points} and yours are {user_points}\n\n")

    elif ip == 's' and random_ == 'w':
        user_points += 1
        print(f"Your guess is {ip} and Comp guess is {random_}\n")
        print('You won 1 point')
        print(f"Comp points are {comp_points} and yours are {user_points}\n\n")

    elif ip == 'w' and random_ == 's':
        comp_points += 1
        print(f"Your guess is {ip} and Comp guess is {random_}\n")
        print('Comp wins 1 point')
        print(f"Comp points are {comp_points} and yours are {user_points}\n\n")

    elif ip == 'w' and random_ == 'g':
        user_points += 1
        print(f"Your guess is {ip} and Comp guess is {random_}\n")
        print('You won 1 point')
        print(f"Comp points are {comp_points} and yours are {user_points}\n\n")

    elif ip == 'g' and random_ == 's':
        user_points += 1
        print(f"Your guess is {ip} and Comp guess is {random_}\n")
        print('You won 1 point')
        print(f"Comp points are {comp_points} and yours are {user_points}\n\n")

    elif ip == 'g' and random_ == 'w':
        comp_points += 1
        print(f"Your guess is {ip} and Comp guess is {random_}\n")
        print('Comp wins 1 point')
        print(f"Comp points are {comp_points} and yours are {user_points}\n\n")

    else:
        print("Invalid choice \n")
        print(f"Your guess {ip} and Computer guess is {ip} \n")

    no_of_chances += 1
    print(f"{chance - no_of_chances} is left out of {chance}")

print("\n\t\t GAME OVER..! !!\n")

if comp_points == user_points:
    print("It's a tie\n")

if comp_points > user_points:
    print("Computer Wins..!!")
print("You won..! !!")

print(f"Your points are {user_points} and comp points are {comp_points}\n")
#
# ########################### to lower input
#
# # list1 = ['s', 'w', 'g']
# #
# # chance = 5
# # no_of_chances = 0
# # comp_points = 0
# # user_points = 0
#
# print("\t\t Snake | Water | Gun Game with Computer\n")
# print("\t\t S for Snake | W for Water | G for Gun \n")
#
# while chance != 0:
#     ip = str(input('S | W | G :'))
#     if ip.lower() in i:
#         comp_choice = random.choice(i)
#         chance -= 1
#
#         if ip == comp_choice:
#             print("No one wins")
#
#         elif comp_choice == 's' and ip.lower() == 'w':
#             print(f"Your guess is {ip} and Comp guess is {comp_choice}\n")
#             print('Comp wins 1 point')
#             print(f"Comp points are {comp_points} and yours are {user_points}\n\n")
#             comp_points += 1
#
#         elif comp_choice == 'w' and ip.lower() == 'g':
#             print(f"Your guess is {ip} and Comp guess is {comp_choice}\n")
#             print('Comp wins 1 point')
#             print(f"Comp points are {comp_points} and yours are {user_points}\n\n")
#             comp_points += 1
#
#         elif comp_choice == 'g' and ip.lower() == 's':
#             print(f"Your guess is {ip} and Comp guess is {comp_choice}\n")
#             print('Comp wins 1 point')
#             print(f"Comp points are {comp_points} and yours are {user_points}\n\n")
#             comp_points += 1
#
#         else:
#             print(f"Your guess is {ip} and Comp guess is {comp_choice}\n")
#             print(f"You won 1 point\n")
#             user_points += 1
#
#     else:
#         print("Invalid Input!!", ip)
#
# if comp_points > user_points:
#     print("Computer won the game...")
# else:
#     print("You won the game...")
