# Time Challenge
"""
Ask the user for a number of seconds
Output the number of whole minues and leftover seconds
e.g. 125 -> 2 minute(s) 5 second(s)
"""
seconds = int(input("Please enter number of seconds: "))

mins = seconds // 60
secs = seconds % 60

print(mins, "minute(s)", secs, "second(s)")