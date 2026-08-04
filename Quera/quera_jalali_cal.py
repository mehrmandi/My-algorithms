
# فرض می کنیم تا عدد 33 را توانسته ایم بسازیم پس 3 ضلع تاس اول 1و 2 و 3 هستند
# و همچنین است برای تاس دوم پس سر جمع در تاس اول و دوم 6 موقعیت خالی داریم در حالیکه برای ساخت اعداد 1 تا 10
# حداقل به 7 ضلع دیگر به غیر از 1و 2 و 3 احتیاج است
# پس طبق برهان خلف ما با دو تاس نهایتا فقط قادر خواهیم بود تا عدد 33 را بسازیم


#  ask the user for input
x = int(input())

#  Let's assume that the numbers of two dice are like this
first_dice = [0, 0, 5, 3, 2, 4]
second_dice = [1, 1, 6, 7, 8, 9]


#  We define a function to find the possibility or not to show a number, which is the input of the number entered by the user
#  If the number is displayable: the numbers of each dice are displayed on each line print
#  If the number cannot be displayed: the number -1 will be shown in the printout
def dice_select(user_num):
    if user_num < 10:
        return first_dice, second_dice
    else:
        for j in first_dice:
            for n in second_dice:
                if user_num == 10 *j + n or user_num == 10 *n + j:
                    return first_dice, second_dice
        else:
            return False



if dice_select(x):
    result = dice_select(x)
    print(*result[0], sep=" ")
    print(*result[1], sep=" ")
else:
    print(-1)


#  --------------------------------------------------------------------------------------------
