# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date(days):
    """Calculate and display the future date after adding the specified number of days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    display_current_datetime()
    
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)

if __name__ == "__main__":
    main()