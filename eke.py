import calendar
import datetime

# Function to get the Igbo day of the week (Eke, Orie, Nkwo, Afor)
def get_igbo_day(date):
    # Define a start date in the Gregorian calendar and its corresponding Igbo day
    start_date = datetime.date(2023, 12, 1)  # This could be any date you choose
    start_day = 'Eke'  # Assume the start date corresponds to 'Eke'

    # Map the Igbo days to an index (0 = Eke, 1 = Orie, 2 = Nkwo, 3 = Afor)
    igbo_days = ['Eke', 'Orie', 'Nkwo', 'Afor']

    # Calculate the number of days difference between the input date and the start date
    delta = (date - start_date).days

    # Determine the day of the Igbo week using modulo operation
    igbo_day_index = (igbo_days.index(start_day) + delta) % 4

    return igbo_days[igbo_day_index]

# Function to convert month name or short form to month number
def month_name_to_number(month_name):
    month_names = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12,
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }
    return month_names.get(month_name.capitalize())

# Function to print the full calendar for a given month and year
def print_igbo_calendar(year, month):
    # Get the first day of the month and the number of days in the month
    first_day, num_days = calendar.monthrange(year, month)

    # Print the header for the calendar
    print(f"Igbo Calendar for {calendar.month_name[month]} {year}")
    print("Mon   Tue   Wed   Thu   Fri   Sat   Sun")

    # Fill the first week with blanks for days before the 1st of the month
    days_in_week = ['   '] * first_day
    igbo_days_in_week = [''] * first_day  # To hold the Igbo days corresponding to each date

    # Iterate through all the days of the month and print the corresponding Igbo day
    for day in range(1, num_days + 1):
        date = datetime.date(year, month, day)
        igbo_day = get_igbo_day(date)
        
        # Add the day to the current week
        days_in_week.append(f"{day:2d} ")
        igbo_days_in_week.append(f"{igbo_day[:3]} ")

        # If we reach the end of the week, print both days and Igbo days
        if len(days_in_week) == 7:
            print("   ".join(days_in_week))  # Print the days of the week
            print("   ".join(igbo_days_in_week))  # Print the Igbo days
            # Reset for the next week
            days_in_week = []
            igbo_days_in_week = []

    # Print any remaining days in the last week
    if days_in_week:
        print("  ".join(days_in_week))
        print("  ".join(igbo_days_in_week))

# Get user input for the month and year
try:
    month_input = input("Enter the month (either number 1-12, full name e.g., January or short form e.g., Jan): ")
    
    # Check if the input is a number (1-12)
    if month_input.isdigit():
        month = int(month_input)
        if 1 <= month <= 12:
            year = int(input("Enter the year (e.g., 2024): "))
            print_igbo_calendar(year, month)
        else:
            print("Invalid month number. Please enter a number between 1 and 12.")
    else:
        # If the input is a name or short form, convert it to a number
        month = month_name_to_number(month_input)
        if month:
            year = int(input("Enter the year (e.g., 2024): "))
            print_igbo_calendar(year, month)
        else:
            print("Invalid month name or short form. Please enter a valid month.")
        
except ValueError:
    print("Invalid input. Please enter valid integers for the year.")
