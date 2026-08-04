x = int(input())

#  store both sides of the dice as keys and values in the dictionary
dice_dict = {1: 6, 3: 4, 2: 5, 6: 1, 4: 3, 5: 2}

#  We design a function that takes the number of one side of the dice and prints the number of the other side, and if the number entered in the dice does not exist, it takes the number from the user again.
def dice_side(user_num):
    print(dice_dict[user_num])


dice_side(x)




