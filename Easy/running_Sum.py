nums = [3,1,2,10,1]

def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

print(running_sum(nums))
