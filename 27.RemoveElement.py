def removeElement(nums:list[int], val: int) -> int:
  k = 0
  for number in range(len(nums)):
    if nums[number] != val:
      nums[k] = nums[number]
      k += 1
  return k

print(removeElement(nums=[1,1,2,2,2,3,3,3,5,5,5,6,6,6], val=3))