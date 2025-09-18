DAYS_IN_MONTH = 30

# Basic inputs 
book_name = input("Enter book name: ")
pages_per_book = float(input("Enter books pages: "))
pages_read_per_day = float(input("How many pages per day?: "))

# Calculate actual read time

average_time_taken_read = pages_per_book / pages_read_per_day 

# if read time exceeds one month, give the extra days needed
# in order to read the book

needed_days = DAYS_IN_MONTH - average_time_taken_read 

#If read time is more than one month, give the extra days needed. So, one month + extra days in order to read
# the actual book

if average_time_taken_read > DAYS_IN_MONTH:
    print(f"You'll need exactly {int(abs(needed_days))} more days in order to read {book_name} for a month")

elif average_time_taken_read <= pages_per_book:
    print(f"You would have enough time to read {book_name}")
