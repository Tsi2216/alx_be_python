# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = ""

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level."

# Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Provide the customized reminder
print("Reminder:", reminder)