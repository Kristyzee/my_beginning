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
        "la": ["", "Ianuarius", "Februarius", "Martius", "Aprilis", "Maius", "Iunius", "Quintilis", "Augustus", "September", "October", "November", "December"]
    }

    short_month_names = {
        "en": ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "fr": ["", "jan", "févr", "mars", "avr", "mai", "juin", "juil", "août", "sept", "oct", "nov", "déc"],
        "de": ["", "Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"],
        "es": ["", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"],
        "la": ["", "Ian", "Feb", "Mar", "Apr", "Mai", "Iun", "Qui", "Aug", "Sep", "Oct", "Nov", "Dec"]
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

# Function to get weekday names in the selected language
def get_weekday_names(language="en"):
    weekday_names = {
        "en": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "fr": ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"],
        "de": ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"],
        "es": ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
        "la": ["Lun", "Mar", "Mer", "Qui", "Fri", "Sab", "Dom"]
    }
    return weekday_names.get(language, weekday_names["en"])

# Function to get day numbers (1-31) in the selected language
def get_day_numbers(language="en"):
    day_numbers = {
        "en": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        "fr": ["un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "trieze", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf", "vingt", "vingt-un", "vingt-deux", "vingt-trois", "vingt-quatre", "vingt-cinq", "vingt-six", "vingt-sept", "vingt-huit", "vingt-neuf", "trente", "trente-un"],
        "de": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        "es": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        "la": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXI"]
    }
    return day_numbers.get(language, day_numbers["en"])

# Function to print the calendar for a specific month with Igbo days
def print_igbo_calendar(year, month, language="en"):
    weekday_names = get_weekday_names(language)
    day_numbers = get_day_numbers(language)
    igbo_days = ['Eke', 'Orie', 'Nkwo', 'Afor']  # Igbo day names

    month_names = {
        "en": calendar.month_name,
        "fr": ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
        "de": ["", "januar", "februar", "märz", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "dezember"],
        "es": ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
        "la": ["", "Ianuarius", "Februarius", "Martius", "Aprilis", "Maius", "Iunius", "Quintilis", "Augustus", "September", "October", "November", "December"]
    }

    first_day, num_days = calendar.monthrange(year, month)
    print(f"\n Calendar for {month_names[language][month]} {year}")
    print("    ".join(weekday_names))  # Print weekday names in the selected language

    # Now we print the day numbers
    days_in_week = ['     '] * first_day
    igbo_days_in_week = ['   '] * first_day  # For Igbo days

    for day in range(1, num_days + 1):
        # Get the Igbo day corresponding to the current date
        date = datetime.date(year, month, day)
        igbo_day = get_igbo_day(date)
        
        # Get the day number from the translated list
        day_str = f"{day_numbers[day - 1]:2}"  
        
        # Append the day number and the corresponding Igbo day to their respective lists
        days_in_week.append(day_str)
        igbo_days_in_week.append(igbo_day)

        if len(days_in_week) == 7:
            print("   ".join(days_in_week))
            print("   ".join(igbo_days_in_week))  # Print the Igbo days below the day numbers
            days_in_week = []
            igbo_days_in_week = []

    # If there are remaining days in the week, print them
    if days_in_week:
        print("   ".join(days_in_week))
        print("   ".join(igbo_days_in_week))

# New function to print the full year's calendar with Igbo days
def print_full_year_calendar(language="en"):
    year = int(input("Enter the year: "))
    print(f"\nFull Calendar for the year {year}:")
    for month in range(1, 13):
        print_igbo_calendar(year, month, language)

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
        month_input = input("Enter month (either number 1-12, full name e.g., January or short form e.g., Jan): ").strip().lower()
        if month_input.isdigit():
            month = int(month_input)
        else:
            month = month_name_to_number(month_input, language_input)
        
        if month == -1:
            print("Invalid month input.")
        else:
            year = int(input("Enter the year (e.g., 2024): "))
            print_igbo_calendar(year, month, language_input)

    elif choice == "2":
        print_full_year_calendar(language_input)

    elif choice == "3":
        print_full_year_calendar(language_input)

    else:
        print("Invalid option. Please choose 1, 2, or 3.")

