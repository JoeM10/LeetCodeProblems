# class Solution:
def removeDuplicates(nums):
  k = 1
  for number in range(1,len(nums)):
    if nums[number] != nums[number-1]:           
      nums[k] = nums[number]              
      k += 1                         
  return k

print(removeDuplicates(nums=[1,1,3,3,4,5]))