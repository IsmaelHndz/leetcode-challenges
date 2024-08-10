class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if target - nums[i] == nums[j]:
                    return [i,j]

                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []

if __name__=="__main__":
   nums = [2,5,5,11]
   target = 10
   solution = Solution()
   print(solution.twoSum(nums, target))

