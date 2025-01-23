def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_week(date):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    f = k + k // 4 + j // 4 - 2 * j + 13 * (month + 1) // 5 + day - 1
    return days[f % 7]

n = int(input())
for _ in range(n):
    date = input()
    print(day_of_week(date))