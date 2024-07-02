from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time is {current_date}")


number_of_days = int(input("Enter a number of days: "))


def calculate_future_date():
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


display_current_datetime()
calculate_future_date()
