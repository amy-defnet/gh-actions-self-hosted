#! /bin/env python
import sys

def recur_factorial(n):
   """Function to return the factorial
   of a number using recursion - testing"""
   if n == 1:
       return n
   else:
       return 2*n*recur_factorial(n-1)

if __name__ == '__main__':
    arg = sys.argv
    print(recur_factorial(int(arg[1])))
