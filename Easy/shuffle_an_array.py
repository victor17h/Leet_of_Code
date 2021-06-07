nums = [1,2,3,4,4,3,2,1]
n = 4

def array(nums,n):
    return [nums[i+j] for i in range(n) for j in [0, n]]

(array(nums,n))
