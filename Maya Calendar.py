haab_months = {
    'pop': 0, 'no': 1, 'zip': 2, 'zotz': 3, 'tzec': 4,
    'xul': 5, 'yoxkin': 6, 'mol': 7, 'chen': 8, 'yax': 9,
    'zac': 10, 'ceh': 11, 'mac': 12, 'kankin': 13, 'muan': 14,
    'pax': 15, 'koyab': 16, 'cumhu': 17, 'uayet': 18
}

tzolkin_names = [
    'imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok',
    'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau'
]

n = int(input())
dates = [input().strip() for _ in range(n)]

def haab_to_days(date):
    day, month, year = date.split()
    day = int(day[:-1])
    month = haab_months[month]
    year = int(year)

    total_days = year * 365 + (month * 20 + day if month < 18 else 18 * 20 + day)
    return total_days


def days_to_tzolkin(days):
    number = (days % 13) + 1
    name = tzolkin_names[days % 20]
    return f"{number} {name} {days // 260}"

results = [days_to_tzolkin(haab_to_days(date)) for date in dates]

print(n)
for result in results:
    print(result)