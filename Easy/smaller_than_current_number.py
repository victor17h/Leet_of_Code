nums = [8,1,2,2,3]

def smaller_numbers(nums):
    numsCount = {}

    for i, number in enumerate(sorted(nums)):
        if number not in numsCount:
            numsCount[number] = i
            print(numsCount)

    for i, number in enumerate(nums):
        nums[i] = numsCount[number]

    return nums



print(smaller_numbers(nums))