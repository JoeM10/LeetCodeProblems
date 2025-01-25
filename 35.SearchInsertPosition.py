def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        newNums= nums
        newNums = sorted(newNums)
        return newNums.index(target)


# Test cases
print(searchInsert(nums=[1,3,5,6], target=5))
print(searchInsert(nums=[1,3,5,6], target=2))
print(searchInsert(nums=[1,3,5,6], target=7))