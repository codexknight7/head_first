# =============================================================================
# This application is doing the following:
# 1) Generates a list with odd numbers from 1 to 60
# 2) Takes the current minute from system date and time and checks
# if this value is present in the list of odd numbers.
# 3) Generates random number of seconds to wait until the next iteration
# 4) Displays a countdown of seconds remaining to wait
# 5) Repeat the process for 5 times
# *****
# author: Konstantin Pankratov
# date: 2024-03-27
# =============================================================================

from datetime import datetime
import random
import time
import sys

odds = [];

for i in range (60):
    if i % 2 != 0:
        odds.append(i)

#for j in odds:
#    print(f"\n {j}")

for  i in range(5):
    current_minute = datetime.today().minute
    if current_minute in odds:
        print(f"\n{current_minute} : This minute is odd.")
    else: 
        print(f"\n{current_minute} : Not an odd minute.")
    
    wait_time = random.randint(1,60)
    print(f"Waiting for another {wait_time} seconds...")
    for t in range(wait_time, 0, -1):
        sys.stdout.write("\b" * len(str(t+1)))  # Move cursor back
        sys.stdout.write(" " * len(str(t+1)))   # Overwrite with spaces
        sys.stdout.write("\b" * len(str(t+1)))  # Move cursor back again
        sys.stdout.write(str(t))             # Print the new number
        sys.stdout.flush()                   # Flush the output
        time.sleep(1)                        # Wait for 1 second
  