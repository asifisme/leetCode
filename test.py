# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return '' 
        
#         def exten(s: str, i : int , j : int):
#             while j >= 0 and j < len(s):
#                 if s[i] != s[j]:
#                     break 
#                 i -= 1 
#                 j += 1 
#             return i + 1, j - 1 

#         for i in range(len(s)):
#             pass  

""" first problem done """

import math 

# area = input("Give the area :) ") 

# area = round(math.pi * (float(area) ** 2), 2)

# print(f'Area = {area}') 

""" Second problem """ 
import datetime 

date = datetime.datetime.now() 

# print(date)

""" Reverse full name """ 

# name = input('Give your full name : ') 

# # print(name[::-1])

# rev = '' 

# for i in name:
#     rev = i + rev 

# print(rev)

file_name = input("Give input file Name : ") 

print(file_name.split('.')[-1])