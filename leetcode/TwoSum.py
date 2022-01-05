def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    print(hashmap)
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


a = [1, 3, 5, 2, 4, 6]
target = 11
print(f"target acquired: {twoSum(a, target)}")
