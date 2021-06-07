nums = [2,7,11,15]
result = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == result:
            print(nums[i], '+', nums[j], '=', result)

def find_sum(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == result:
                return f'{nums[i]} + {nums[j]} = {result}'

print(find_sum(nums))