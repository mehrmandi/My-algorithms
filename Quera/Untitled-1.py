x = input(int(input("write a number please:")))
first_dice = [1, 2, 3, 4, 5, 8]
second_dice = [0, 1, 2, 7, 6, 9]

def dice_select(x):
    flag = True
    print(flag)
    for j in first_dice:
        for n in second_dice:
            while flag:
                if x == 10*j + n or x == 10*n + j:
                    print(first_dice, second_dice, sep="\n")
                    flag = False
            else:
                print("-1")



dice_select(x)