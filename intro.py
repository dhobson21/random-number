# Use the following code to create a list of 10 random numbers. Each number will be between 0 and 6.

import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

    # Then iterate a different list of numbers that are sequential from 1 to 10.

"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""
for number in range(1, 10):
        if my_randoms.count(number) > 0:
            print(f"my_randoms list contains {number}")
        else:
            print(f"my_randoms list does not contain {number}")
