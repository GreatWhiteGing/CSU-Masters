# get the current time in 24-hour format
current_time = int(input("What time is it? (24 hour): "))
# ask how long they want to wait for alarm
wait_for_alarm = int(input("How many hours would you like to wait for your alarm?: "))
# calculates how many hours alarm needs to wait (in 24-hour increments)
alarm_go_off = (current_time + wait_for_alarm) % 24
# checks to see if there is any need to wait for alarm
if wait_for_alarm == 0:
    print("Your alarm is already ringing")
else:
    # if there is, displays when the alarm will go off
    print(f"The alarm will sing at {alarm_go_off}:00")
