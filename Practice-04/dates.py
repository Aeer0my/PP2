# dates.py
# Python Date and Time exercises

from datetime import datetime, timedelta


# Exercise 1: Subtract five days from the current date
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print("Exercise 1 — Subtract 5 days from today:")
print(f"  Today:      {today.strftime('%Y-%m-%d')}")
print(f"  5 days ago: {five_days_ago.strftime('%Y-%m-%d')}")


# Exercise 2: Print yesterday, today, and tomorrow
yesterday  = today - timedelta(days=1)
tomorrow   = today + timedelta(days=1)
print("\nExercise 2 — Yesterday, Today, Tomorrow:")
print(f"  Yesterday: {yesterday.strftime('%Y-%m-%d')}")
print(f"  Today:     {today.strftime('%Y-%m-%d')}")
print(f"  Tomorrow:  {tomorrow.strftime('%Y-%m-%d')}")


# Exercise 3: Drop microseconds from datetime
now_with_microseconds    = datetime.now()
now_without_microseconds = now_with_microseconds.replace(microsecond=0)
print("\nExercise 3 — Drop microseconds:")
print(f"  With microseconds:    {now_with_microseconds}")
print(f"  Without microseconds: {now_without_microseconds}")


# Exercise 4: Calculate difference between two dates in seconds
date1 = datetime(2024, 1, 1, 0, 0, 0)
date2 = datetime(2024, 1, 10, 12, 30, 0)
difference = date2 - date1
total_seconds = int(difference.total_seconds())
print("\nExercise 4 — Date difference in seconds:")
print(f"  Date 1: {date1}")
print(f"  Date 2: {date2}")
print(f"  Difference: {total_seconds} seconds")
