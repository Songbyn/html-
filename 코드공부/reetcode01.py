def twoSum(nums, target) :
    hash = {}
    for i,v in enumerate(nums) :
        if target - v in hash :
            return [i,hash[target-v]]
        hash[v] = i
    return []

print(twoSum([2,5,11,15],9))
    
        