#https://www.hackerrank.com/challenges/utopian-tree/problem
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
# This is a function named 'utopianTree'. It takes one input, 'n'.
# 'n' is the number of growth cycles for the tree.
def utopianTree(n):
    # The tree starts with a height of 1 meter.
    height = 1

    # We use a loop to go through each growth cycle.
    # The loop runs from 1 to 'n'.
    for cycle in range(1, n + 1):
        # If the cycle number is odd, it is spring.
        if cycle % 2 == 1:
            # In spring, the tree doubles in height.
            height *= 2  # height = height * 2
        else:
            # If the cycle number is even, it is summer.
            # In summer, the tree grows 1 meter taller.
            height += 1  # height = height + 1

    # After all cycles, we return the final height of the tree.
    return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
