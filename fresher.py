import time

task = input("Enter the task you need to be reminded about: ")
interval = int(input("Enter the reminder interval in minutes: "))

while True:
    print("Reminder:", task)
    time.sleep(interval * 60)