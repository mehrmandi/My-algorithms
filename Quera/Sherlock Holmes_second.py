
import random
import math

letters = "acdefghijlmnopqrstuvwxyz"
random_letters = []


#  k is sherlock speed in 1 second
k = int(input())
#  b is number of buildings
b = int(input())

# Generate b Random letters except of k and b
for i in range(b):
    random_letter = random.choice(letters)
    random_letters += random_letter

#  random letters are the height of buildings in order


#  define a function to calculate seconds that Sherlock can achieve Moriarty
def sherlock_time():
    sum = math.ceil(random_letters[b - 1] / k) + b
    prev = 0
    for i in random_letters:
        height = math.ceil(abs(i - prev) / k)
        prev = i
        sum += height
    print(sum)

sherlock_time()









