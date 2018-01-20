nums = [2,5,2,56,8,4,2,5,6]
j = 0
total = 0
while j < len(nums):
    total += nums[j]
    j += 1

print("avg:" + str (total /len(nums)))