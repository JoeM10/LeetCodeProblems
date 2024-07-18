def findMaxK(nums: list[int]) -> int:
    otherList = []
    k = -1
    for number in nums:
        if number * -1 in otherList and abs(number) > k:
            k = abs(number)
            otherList.append(number)
        
        else:
            otherList.append(number)
    return k

print(findMaxK([-1,2,-3,3]))
print(findMaxK([-1,10,6,7,-7,1]))
print(findMaxK([-10,8,6,7,-2,-3]))