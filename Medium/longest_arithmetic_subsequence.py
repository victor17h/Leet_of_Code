nums = [3,6,9,12]


def subsequence(nums):
    lasnum = []
    maxEnc = 0
    for i in range(len(nums)):
        dictio = {}
        for j in range(i):
            if (nums[i] - nums[j]) in lasnum[j]:
                newval = lasnum[j][nums[i]-nums[j]]+1
            else:
                newval = 2
            maxEnc = max(maxEnc,newval)
            dictio.update({nums[i]-nums[j]:newval})
        lasnum.append(dictio)
    return maxEnc


print(subsequence(nums))
