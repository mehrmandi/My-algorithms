import  math

#  Number of hours required to complete the project
n = int(input())
#  minimum hours of work per day
#  maximum hours of work per day
min_hour, max_hour = [int(x) for x in input().split(" ")]


#  define a function that calculate minimum number of days for done project
def minDay(project, min, max):
    coe = int(project / min)
    if coe * max < project:
        print(-1)
    else:
        day = math.ceil(project / max)
        print(day)


minDay(n, min_hour, max_hour)



