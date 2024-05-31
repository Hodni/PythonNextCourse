def gen_secs():
    """Generate all possible seconds (0 to 59)."""
    for sec in range(60):
        yield sec


def gen_minutes():
    """Generate all possible minutes (0 to 59)."""
    for min in range(60):
        yield min


def gen_hours():
    """Generate all possible hours (0 to 23)."""
    for hour in range(24):
        yield hour


def gen_time():
    """Generate all possible times in a day from 00:00:00 to 23:59:59."""
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02d}:{minute:02d}:{second:02d}"


def gen_years(start=2024):
    """Generate years starting from a specific year."""
    while True:
        yield start
        start += 1


def gen_months():
    """Generate all months (1 to 12)."""
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """Generate days in a given month."""
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }
    for day in range(1, days_in_month[month] + 1):
        yield day


def gen_date():
    """Generate full date-time stamps in the format dd/mm/yyyy hh:mm:ss."""
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield f"{day:02d}/{month:02d}/{year} {time}"


def print_all_dates():
    """Print every millionth date generated."""
    date_generator = gen_date()
    count = 0
    for date in date_generator:
        count += 1
        if count % 1000000 == 0:
            print(date)


# Run the function to start generating and printing dates
print_all_dates()
