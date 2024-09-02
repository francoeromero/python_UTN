
'''
factorial
0! = 1
1! = 1
2! = 2 x 1 = 2
3! = 3 x 2 x 1 = 6
4! = 4 x 3 x 2 x 1 = 24

for i in range(10, 0, -1):
    print(i)

10,9,8,7.. 1
'''
# # FACTORIAL WITHOUT RECURSION

# def factorial(n:int):
#     a = 1
#     if n == 1 or n == 0:
#         return 1
#     else:
#         for i in range(n, 1, -1):
#             a = a * i
#         return a
# print(factorial(3))

# # FACTORIAL WITH RECURSION

# def factorial_recursion(n:int):
#     if n == 0:
#         r = 1
#     else:
#         r= n * factorial_recursion(n-1)
#     return r

# # RECURSION

# def decrement(num:int)->int:
#     '''
#     Recursion:
#     Decrement a number from 'num' to 0  
#     '''
#     if num == 0 :
#         r = num
#     else:
#         print(num)
#         r = decrement(num-1)
#     return r
# decrement(3)


# # count from 0 to 3

# initial = 0
# def increase(initial:int,num:int)->int:
#     '''
#     Recursion:
#     Increase a number from zero to 'num'
#     '''
#     if initial < num:
#         print(initial)
#         increase(initial+1,num)
#     else:
#         print(num)
#         return num

# increase(0,3)


# sum nature numbers 3 = 3+2+1 = 6

# def sum_without_recursion(num:int):
#     a = 0
#     for i in range(0, num):
#         a = a + num
#         num = num - 1 
#     return a 
# print(sum_without_recursion(3))

def sum_with_recursion(num:int):
    if num == 0:
        r = 0
    else:
        r = num + sum_with_recursion(num-1)
    return r

# # SUM DIGITS

# def sum(num:int):
#     str_num = str(num)
#     digits = len(str_num)
#     a = 0
#     for i in range(0,digits):
#         int_num = int(str_num[i])
#         a += int_num
#     return a
# print(sum(212))