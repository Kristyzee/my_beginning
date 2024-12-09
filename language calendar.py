import calendar
import datetime

# Function to get the Igbo day of the week (Eke, Orie, Nkwo, Afor)
def get_igbo_day(date):
    start_date = datetime.date(2023, 12, 1)  # This could be any date you choose
    start_day = 'Eke'  # Assume the start date corresponds to 'Eke'
    igbo_days = ['Eke', 'Orie', 'Nkwo', 'Afor']
    
    # Calculate the number of days difference between the input date and the start date
    delta = (date - start_date).days
    igbo_day_index = (igbo_days.index(start_day) + delta) % 4
    return igbo_days[igbo_day_index]

# Function to convert month name or short form to month number, handling different languages
def month_name_to_number(month_name, language="en"):
    month_names = {
        "en": ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "fr": ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
        "de": ["", "januar", "februar", "märz", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "dezember"],
        "es": ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
        "la": ["", "Ianuarius", "Februarius", "Martius", "Aprilis", "Maius", "Iunius", "Iulius", "Augustus", "September", "October", "November", "December"]
    }

    short_month_names = {
        "en": ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "fr": ["", "jan", "févr", "mars", "avr", "mai", "juin", "juil", "août", "sept", "oct", "nov", "déc"],
        "de": ["", "Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"],
        "es": ["", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"],
        "la": ["", "Ian", "Feb", "Mar", "Apr", "Mai", "Iun", "Iul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    }

    # Normalize the input to lowercase for case-insensitive comparison
    month_name = month_name.strip().lower()

    # First check for the full month name (case-insensitive)
    for i, month in enumerate(month_names[language]):
        if month.lower() == month_name:
            return i

    # Then check for the short month name (case-insensitive)
    for i, month in enumerate(short_month_names[language]):
        if month.lower() == month_name:
            return i

    return -1  # Invalid month name

# Function to print the calendar for a specific month with Igbo days
def print_igbo_calendar(year, month, language="en"):
    month_names = {
        "en": calendar.month_name,
        "fr": ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
        "de": ["", "januar", "februar", "märz", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "dezember"],
        "es": ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
        "la": ["", "Ianuarius", "Februarius", "Martius", "Aprilis", "Maius", "Iunius", "Iulius", "Augustus", "September", "October", "November", "December"]
    }

    first_day, num_days = calendar.monthrange(year, month)
    print(f"\n Calendar for {month_names[language][month]} {year}")
    print("Mon    Tue    Wed    Thu    Fri    Sat    Sun")

    days_in_week = ['   '] * first_day
    igbo_days_in_week = [''] * first_day  # To hold the Igbo days corresponding to each date

    for day in range(1, num_days + 1):
        date = datetime.date(year, month, day)
        igbo_day = get_igbo_day(date)

        days_in_week.append(f"{day:2d} ")
        igbo_days_in_week.append(f"{igbo_day[:3]} ")

        if len(days_in_week) == 7:
            print("   ".join(days_in_week))
            print("   ".join(igbo_days_in_week))
            days_in_week = []
            igbo_days_in_week = []

    if days_in_week:
        print("  ".join(days_in_week))
        print("  ".join(igbo_days_in_week))

# New function to print the full year's calendar with Igbo days
def print_full_year_calendar(language="en"):
    year = int(input("Enter the year: "))
    print(f"\nFull Calendar for the year {year}:")

    for month in range(1, 13):
        print_igbo_calendar(year, month, language)

# Function to print the calendar for a range of months with Igbo days
def print_calendar_range(language_input):
    try:
        # Get the start and end month from the user
        start_month_input = input("Enter the start month (either number 1-12, full name e.g., January or short form e.g., Jan): ").strip().lower()
        end_month_input = input("Enter the end month (either number 1-12, full name e.g., January or short form e.g., Jan): ").strip().lower()

        # Convert start and end month input to numbers
        if start_month_input.isdigit():
            start_month = int(start_month_input)
        else:
            start_month = month_name_to_number(start_month_input, language_input)
        
        if end_month_input.isdigit():
            end_month = int(end_month_input)
        else:
            end_month = month_name_to_number(end_month_input, language_input)
        
        if start_month == -1 or end_month == -1:
            print("Invalid month input. Please try again.")
            return
        
        # Validate that start month is less than or equal to end month
        if start_month > end_month:
            print("Start month must be less than or equal to end month.")
            return
        
        # Get the year from the user
        year = int(input("Enter the year (e.g., 2024): "))
        
        # Print calendar for each month in the range
        for month in range(start_month, end_month + 1):
            print_igbo_calendar(year, month, language_input)
    except Exception as e:
        print(f"Error occurred: {e}")

# Main program to choose options
if __name__ == "__main__":
    print("Choose an option:")
    print("1. View Calendar for a specific month")
    print("2. View Calendar for a range of months")
    print("3. View full year's calendar")

    choice = input("Enter the option number (1, 2, or 3): ")

    # Language selection with validation
    valid_languages = {"en": "English", "fr": "French", "de": "German", "es": "Spanish", "la": "Latin"}
    
    print("\nChoose language:")
    for code, language in valid_languages.items():
        print(f"{code}: {language}")
    
    language_input = input("\nEnter the language code (e.g., 'en' for English): ").strip().lower()
    
    # If the language input is invalid, default to English
    if language_input not in valid_languages:
        print("Invalid language choice. Defaulting to English.")
        language_input = "en"
    
    if choice == "1":
        year = int(input("Enter the year (e.g., 2024): "))
        month_input = input("Enter the month (either number 1-12, full name e.g., January or short form e.g., Jan): ").strip().lower()
        
        # Check if input is numeric (month number)
        if month_input.isdigit():
            month = int(month_input)
        else:
            # Otherwise, convert month name to number using language input
            month = month_name_to_number(month_input, language_input)
        
        if month != -1 and 1 <= month <= 12:
            print_igbo_calendar(year, month, language_input)
        else:
            print("Invalid month input")
    elif choice == "2":
        print_calendar_range(language_input)
    elif choice == "3":
        print_full_year_calendar(language_input)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
