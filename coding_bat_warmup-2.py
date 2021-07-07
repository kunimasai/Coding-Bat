# def string_times(str, n):
#     return str * n

# def front_times(str, n):
#     if len(str) < 3:
#         return str*n
#     return str[0:3]*n

# def string_bits(str):
#     string = ''
#     i = 0
#     while i < len(str):
#         string = string + str[i]
#         i += 2
#     return string

# print (string_bits('Hello'))

# def string_splosion(str):
#     string = ''
#     i = 0
#     while i < len(str):
#         string = string + str[0:i]
#         i += 1
#     return string + str

# print (string_splosion('ab'))

# def last2(str):
#     last_two = str[len(str)-2:]
#     i = 0
#     count = 0
#     while i < len(str)-2:
#         if str[i:i+2] == last_two:
#             count += 1
#         i += 1
#     return count

# print (last2('axxxaaxx'))

# def array_count9(nums):
#     count = 0
#     for e in nums:
#         if e == 9:
#             count += 1
#     return count

# print (array_count9([1,9,9,3,9]))

# def array_front9(nums):
#     array_len = len(nums)
#     if array_len < 4:
#         for e in nums:
#             if e == 9:
#                 return True
#     for e in nums[:4]:
#         if e == 9:
#             return True
#     return False

# print (array_front9([]))

# def array123(nums):
#     i = 0
#     for e in nums[i:]:
#         print (i)
#         if e == 1:
#             i += 1
#             print (i)
#             for e in nums[i:]:
#                 if e == 2:
#                     i += 1
#                     print (i)
#                     for e in nums[i:]:
#                         if e ==3:
#                             return True
#     return False
    
# print (array123([2,3,4,1,1,2,1,2,3]))

def string_match(a, b):
    len_a = len(a)
    len_b = len(b)
    if (len_a - len_b) < 0:
        smaller = len_a
    else:
        smaller = len_b
    i = 0
    count = 0
    while i < smaller:
        print ("a is:", a[i:i+2])
        print ("b is:", b[i:i+2])
        if len(a[i:i+2]) == 2 and len(b[i:i+2]) == 2:
            if a[i:i+2] == b[i:i+2]:
                count += 1
                print ('count is:', count)
        i += 1
    return count

        
    
print (string_match('abc', 'abc'))