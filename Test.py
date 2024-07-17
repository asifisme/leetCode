# # leet code problem 2806 


# # leetCode 3005 problem not solved 
# def Sol(num : list):
#     dic = {} 

#     for i in num:
#         if i in dic:
#             dic[i] += 1 
#         else:
#             dic[i] = 1 

#     m = max(dic.values()) 

#     return sum((i == m for i in dic.values())) 




    
#     # return sum(f == m for f in dic.values()) * m 
            



# if __name__ == "__main__":
#     # num = [1,2,3,4,5] 
#     #num = [1,2,2,3,1,4]
#     num = [1,2,2,3,1,4]
#     #num = [17,17,2,12,20,17,12]
#     print(Sol(num))

# import collections 


# cnt = collections.Counter()
# res = {}
# for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#     cnt[word] += 1

# l = ['red', 'blue', 'red', 'green', 'blue', 'blue']

# for i in l:
#     if i in res:
#         res[i] += 1 
#     else:
#         res[i] = 1 

# print(cnt)
# print(res) 

nums = 14 
nums_ = 10 

print(nums & nums_) 
print(nums and nums_ ) 
print(nums | nums)
