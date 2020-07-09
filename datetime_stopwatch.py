#! /usr/bin/env python3
# datetime_stopwatch.py - Create a stopwatch using datetime

from datetime import datetime
print("""Let's see how long it takes for you to type your full name!
The timer is starting now.""")

now = datetime.now()
to_do = input('Type in your full name: ')
end = datetime.now()
total_time = end - now
print('It took you ' + str((total_time).seconds) + ' seconds to type your full name.')
