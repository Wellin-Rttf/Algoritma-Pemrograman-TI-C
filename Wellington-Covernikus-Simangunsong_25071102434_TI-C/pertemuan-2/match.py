# Daripada menggunakan banyak if-else, kita dapat menggunakan statement match
"""
Sintaks:
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
"""

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")


# Default Value
# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")


# Combine Values
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:           #Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")