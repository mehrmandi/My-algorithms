import random
import math

letters = "abcdefghijlmopqrstuvwxyz"
random_letters = []

#  n is the number of quera employees
#  k is the capacity of the cinema
n, k = [int(i) for i in input().split(" ")]

# Generate n Random letters except of k and n
for i in range(n):
    random_letter = random.choice(letters)
    random_letters += random_letter

#  random letters are the number of employee's friends
friends_sorted = [int(num) for num in input().split(" ")]
friends_sorted.sort()

#  calculate max number of employees that can go to cinema with them friends
def maxEmployee(quera_num, cinema_cap):
    max_employee = 0
    while quera_num > 0:
        cinema_cap -= friends_sorted[max_employee] + 1
        if cinema_cap < 0:
            break
        max_employee += 1
        quera_num -= 1
    print(max_employee)


maxEmployee(n, k)






