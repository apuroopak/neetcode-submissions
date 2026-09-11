class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = []
        found = False
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    sum = [i,j]
                    found = True
                    break
            
            if found:
                break
        
        return sum
                
                

