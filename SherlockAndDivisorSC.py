#!/bin/python3

import math
import os
import random
import re
import sys

def divisors(n):
    count = 0  
    for i in range(1, int(math.sqrt(n)) + 1):  
        if n % i == 0:  
            if i % 2 == 0:  
                count += 1
            if i != n // i and (n // i) % 2 == 0:  
                count += 1
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  

    for t_itr in range(t):  
        n = int(input().strip())  

        result = divisors(n)  
        fptr.write(str(result) + '\n')  

    fptr.close()  
