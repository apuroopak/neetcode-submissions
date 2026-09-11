class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                # if the middle is the target
                return mid
            
            elif nums[mid] < target:
                # target is in right half
                low = mid + 1

            else:
                # target is in left half
                high = mid - 1
        
        return -1




        