#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#
def matchInt(match_1, match_2):
    return int(match_1 == match_2)


def matchingStrings(strings, queries):
    matches = []
    for query in queries:
        matches.append(0)
        for string in strings:
            matches[-1] += matchInt(query, string)
    
    return matches


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
