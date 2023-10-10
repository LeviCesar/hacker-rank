#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(array: list):
    get_indexes = lambda find, items: [index for (item, index) in zip(items, range(len(items))) if find == item]
    for item in array:
        if len(get_indexes(item, array)) == 1:
            return item

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
