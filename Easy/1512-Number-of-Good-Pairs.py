class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        checked = defaultdict(list)
        
        for i, num in enumerate(nums):
            if num in checked:
                count += len(checked[num])
            checked[num].append(i)
                
        return count