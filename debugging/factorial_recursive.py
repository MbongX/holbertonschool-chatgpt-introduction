#!/usr/bin/python3
import sys

def factorial(n):
 """
 Function Description:
     Calculates the factorial of a number recursively.
 
 Parameters:
     n (int): The number whose factorial will be calculated.
 
 Returns:
     int: The factorial value of the given number.
 """
 if n == 0:
  return 1
 else:
  return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)