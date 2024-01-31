from typing import List

class Solution:
    def moveZeros(self, nums: List[int]):
        j = 0
        for num in nums:
            if (num!=0):
                nums[j]=num
                j+=1
        
        for x in range(j, len(nums)):
            nums[x] = 0
        return nums

objSolutions = Solution()
result = objSolutions.moveZeros([25,9,0,34,56,89,57,0,78,45,72,0,8])
print(result)