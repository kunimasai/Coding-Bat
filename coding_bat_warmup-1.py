# def sleep_in(weekday, vacation):
#     if weekday == False and vacation == False:
#         return True
#     if weekday == True and vacation == False:
#         return False
#     if vacation == True:
#         return True

# print (sleep_in(False, False))
# print (sleep_in(True, False))
# print (sleep_in(False, True))


# def monkey_trouble(a_smile, b_smile):
#     if a_smile == True and b_smile == True:
#         return True
#     if a_smile == False and b_smile == False:
#         return True
#     else:
#         return False

# print (monkey_trouble(True, True))
# print (monkey_trouble(False, False))
# print (monkey_trouble(True, False))

# def sum_double(a,b):
#     if a == b:
#         return (a+b)*2
#     return a+b

# def diff21(n):
#     if n > 21:
#         return (n-21)*2
#     return abs(n-21)

# def parrot_trouble(talking, hour):
#     if hour < 7 or hour > 20:
#         if talking == True:
#             return True
#     return False

# def makes10(a,b):
#     if a == 10 or b == 10:
#         return True
#     if a+b == 10:
#         return True
#     return False

# def near_hundred(n):
#     if abs(100-n) <= 10 or abs(200-n) <= 10:
#         return True
#     return False

# print (near_hundred(201))

# def pos_neg(a, b, negative):
#     if negative == True:
#         if a < 0 and b < 0:
#             return True
#     if a < 0 and b > 0:
#         if negative == False:
#             return True
#     if a > 0 and b < 0:
#         if negative == False:
#             return True
#     return False

# def not_string(str):
#     if str[0:3] == 'not':
#         return str
#     return 'not ' + str

# print (not_string('not candy'))

# def missing_char(str, n):
#     return str[0:n] + str[n+1:]

# print (missing_char('kitten', 1))

# def front_back(str):
#     if len(str) == 1 or len(str) == 0:
#         return str
#     return str[-1] + str[1:-1] + str[0]

# print (front_back(''))

def front3(str):
    if len(str) < 3:
        return str*3
    return str[0:3]*3
