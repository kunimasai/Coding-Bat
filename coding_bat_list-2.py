# def count_evens(nums):
#     count = 0
#     for e in nums:
#         if e%2 == 0:
#             count += 1
#     return count

# print (count_evens([1,3,5]))

# def big_diff(nums):
#     return max(nums) - min(nums)
        
# print (big_diff([7,2,10,9]))

# def centered_average(nums):
#     largest = max(nums)
#     smallest = min(nums)
#     total = 0
#     length = len(nums) - 2
#     for e in nums:
#         total = total + e
#     ignoring_maxmin = total - largest - smallest
#     mean = ignoring_maxmin / length
#     return mean

# print (centered_average([1, 2, 3, 4, 100]))

# def has22(nums):
#     i = 0
#     while i < len(nums)-1:
#         print ('i is: ', i)
#         if nums[i] == 2 and nums[i+1] == 2:
#             return True
#         i += 1
#     return False

def sum13(nums):
    i = 0
    total = 0

    while i < len(nums):
        if nums[i] == 13:
            i += 2
            continue
        total = total + nums[i]
        i += 1
    return total

def sum67(nums):
    i = 0
    total = 0

    while i < len(nums):
        print ('nums is: ', nums)
        print ('nums[i] is: ', nums[i])
        if nums[i] != 6:
            total += nums[i]
            print ('total is: ', total)
        else:
            while nums[i] != 7:
                nums.remove(nums[i])
                print ('nums is: ', nums)
        i += 1
    return total

print (sum67([1,1,6,7,2]))
