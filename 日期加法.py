def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    return 0
def add_days(date,n):
    year,month,day=map(int,date.split('-'))
    while n>0:
        current_month_days=days_in_month(year,month)
        if day+n<=current_month_days:
            day+=n
            n=0
        else:
            n-=(current_month_days-day+1)
            day=1
            if month > 12:
                month -= 12
                year += 1
            else:
                month += 1
    return f"{year:04d}-{month:02d}-{day:02d}"

input_data = input().strip()
n=int(input())
result=add_days(input_data,n)
print(result)