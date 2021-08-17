# import os 

# ar_count = int(input().strip())

# ar = list(map(int, input().rstrip().split()))

# array = []
# for _ in range(3):
#     array.append(list(map(int, input().rstrip().split())))
# print(array)

''' Diagonal array difference '''
# N = int(input().strip())
# total = 0

# for index in range(N):
#     row = input().rstrip().rsplit()
#     total += int(row[index]) - int(row[-(index + 1)])
# print(abs(total))

''' ratio of positive, negative and zero'''
# N = int(input().strip())

# def cal_ratio(arr):
#     new_arr = [1 if int(temp) > 0 else -1 if int(temp) < 0 else 0 for temp in arr]
#     print('{:6f}\n{:6f}\n{:6f}'.format(new_arr.count(1)/N, new_arr.count(-1)/N, new_arr.count(0)/N))

# inital_arr = list(map(int, input().strip().rsplit()))
# cal_ratio(inital_arr)

'''  Building Staircase '''
# def staircase(n):
#     for i in range(1, n + 1):
#         print(' '*(n - i) + '#'*i)
# staircase(7)

''' Sorting an array and finding sum'''
# def miniMaxSum(arr):
#     # Write your code here
#     arr = sorted(arr)
#     total = sum(arr)
#     print(total - arr[-1], total - arr[0])

# miniMaxSum([7, 69, 2, 221, 8974])

''' Find if two words are Anagram '''
# def anagram(word1, word2):

#     word1 = word1.replace(' ','').lower()
#     word2 = word2.replace(' ','').lower()

#     # Validate initial case
#     if len(word1) != len(word2):
#         return False
    
#     count = {}
#     for word in word1:
#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1
    
#     for word in word2:
#         if word in count:
#             count[word] -= 1
#         else:
#             count[word] = 1
    
#     for word in count:
#         if count[word] != 0:
#             return False

#     return True

# print(anagram("DEBIT CARD","BAD CREDkk"))
    
'''Calculating the possible two numbers to sum up to k
input  : sum_number([1,3,2,2], 4)
output : (2,3) 
         (2,2)
'''

# def sum_number(arry, k):
#     if len(arry) < 2:
#         return print("Not enough indexes!")

#     seen = set()
#     output = set()

#     for num in arry:
#         target = k - num
#         if target not in seen:
#             seen.add(num)
#         else:
#             output.add((min(num, target), max(num, target)))

#     print("\n".join(map(str, output)))

# sum_number([1, 2, 3, 4, 5, 6, 7, 8, 10], 10)

''' Add running sum of an array '''
