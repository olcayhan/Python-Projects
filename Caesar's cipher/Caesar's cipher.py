#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
   if k > 26:
        k = k%26

   word = []
   for i in s:
     if ord(i) >=  97 and ord(i)<=122:
        if ord(i)+k > 122:
            word.append(chr(ord(i)-26+k))   
        else:
            word.append(chr(ord(i)+k))
     
        
     elif ord(i) >=  65 and ord(i)<=90:
        if ord(i)+k > 90:
            word.append(chr(ord(i)-26+k)) 
        else:
            word.append(chr(ord(i)+k))
     
     else:
        word.append(i) 
          
   print("".join(word))
if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    caesarCipher(s, k)

