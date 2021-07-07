# def double_char(str):
#     temp = ''
#     for e in str:
#         print (e)
#         temp = temp + e*2
#     return temp

# print (double_char('AAbb'))

# def count_hi(str):
#     count = 0
#     i = 0
#     while i < len(str):
#         if str[i:i+2] == 'hi':
#             count += 1
#         i += 1
#     return count

# print (count_hi('hiabchi hi'))

# def cat_dog(str):
#     cat_count = 0
#     dog_count = 0
#     i = 0
#     j = 0
#     while i < len(str):
#         if str[i:i+3] == 'cat':
#             cat_count += 1
#         i += 1
#     while j < len(str):
#         if str[j:j+3] == 'dog':
#             dog_count += 1
#         j += 1
#     if cat_count == dog_count:
#         return True
#     return False

# print (cat_dog('1cat1cadodog'))

# def count_code(str):
#     # if len(str) < 4:
#     #     return 0
#     i = 0
#     count = 0
#     while i < len(str)-3:
#         if str[i:i+2] == 'co' and str[i+3] == 'e':
#             count += 1
#         i += 1
#     return count

# print (count_code('coz'))

# def end_other(a,b):
#     if len(a) < len(b):
#         shorter = a.lower()
#         longer = b.lower()
#     else:
#         shorter = b.lower()
#         longer = a.lower()
#     if shorter == longer[len(longer)-len(shorter):]:
#         return True
#     return False

# print (end_other('Hiabc', 'abc'))
    
def xyz_there(str):
    i = 0
    count = 0
    while i < len(str):
        print ('i is:', i)
        if str[i:i+3] == 'xyz' and str[i-1] != '.':
            print (str[i:i+3])
            print (str[i-1])
            count += 1
        i += 1
    if count != 0:
        return True
    return False

print (xyz_there('xyz.abc'))