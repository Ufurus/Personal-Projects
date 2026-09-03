import calendar

months = {
    "January" : 31,
    "February" : 28,
    "March" : 31,
    "April" : 30,
    "May" : 31,
    "June" : 30,
    "July" : 31,
    "August" : 31,
    "September" : 30,
    "October" : 31,
    "November" : 30,
    "December" : 31,
}

# for month in months.items():
#     curr_month, days = month

curr_month = calendar.month(2026, 2)
b_month = curr_month[16:140]
final_month = b_month.strip()
print(final_month[18])