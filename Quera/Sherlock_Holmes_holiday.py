import statistics
import math



#  first day of the month
week_day = input()


#  define a list as sample of week days
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#  define a list based on input day
reindex_week = ["a", "b", "c", "d", "e", "f", "g"]

#  define a dictionary that stores the crime rate for each day of the week
crime_rate_day = {"0": [],
                  "1": [],
                  "2": [],
                  "3": [],
                  "4": [],
                  "5": [],
                  "6": []}


#  define a function to reindex the week days based on input day
def weekDayReset(input):
    input_index = week.index(input)
    for day in week:
        day_index = week.index(day)
        if day_index >= input_index:
            reindex_week[day_index - input_index] = day
        else:
            reindex_week[7 - (input_index - day_index)] = day


#  separate the crime rate for each day of the week
for i in range(0, 30):
    crime_rate = int(input())
    if i in (0, 7, 14, 21, 28):
        crime_rate_day["0"].append(crime_rate)
    elif i in (1, 8, 15, 22, 29):
        crime_rate_day["1"].append(crime_rate)
    elif i in (2, 9, 16, 23):
        crime_rate_day["2"].append(crime_rate)
    elif i in (3, 10, 17, 24):
        crime_rate_day["3"].append(crime_rate)
    elif i in (4, 11, 18, 25):
        crime_rate_day["4"].append(crime_rate)
    elif i in (5, 12, 19, 26):
        crime_rate_day["5"].append(crime_rate)
    else:
        crime_rate_day["6"].append(crime_rate)

#  calculate the average crime for each day of the week
mean0 = statistics.mean(crime_rate_day["0"])
mean1 = statistics.mean(crime_rate_day["1"])
mean2 = statistics.mean(crime_rate_day["2"])
mean3 = statistics.mean(crime_rate_day["3"])
mean4 = statistics.mean(crime_rate_day["4"])
mean5 = statistics.mean(crime_rate_day["5"])
mean6 = statistics.mean(crime_rate_day["6"])

mean_array = [mean0, mean1, mean2, mean3, mean4, mean5, mean6]

# calculate the day with minimum of crime rate
def show_min_crime(day):
    weekDayReset(day)
    min_crime = min(mean0, mean1, mean2, mean3, mean4, mean5, mean6)
    index = mean_array.index(min_crime)
    print(reindex_week[index], math.floor(min_crime), sep="\n")

show_min_crime(week_day)

