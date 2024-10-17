#calender range

import calendar


def print_calendar_range():
    year = int(input("Enter the year: "))
    start_month_input = input("Enter the starting month (name or number): ")
    end_month_input = input("Enter the ending month (name or number): ")

    # Convert start month input to integer if it's a number
    if start_month_input.isdigit():
        start_month = int(start_month_input)
    else:
        start_month = list(calendar.month_name).index(start_month_input.capitalize())

    # Convert end month input to integer if it's a number
    if end_month_input.isdigit():
        end_month = int(end_month_input)
    else:
        end_month = list(calendar.month_name).index(end_month_input.capitalize())

    # Print the calendar for each month in the range
    print(
        f"\nThe calender from {calendar.month_name[start_month]} to {calendar.month_name[end_month]} for the year {year} is:  "
    )
    for month in range(start_month, end_month + 1):
        # print("\n", calendar.month_name[month], year)
        # print(calendar.monthcalendar(year, month))
        print("\n", calendar.month(year, month))


print_calendar_range()

