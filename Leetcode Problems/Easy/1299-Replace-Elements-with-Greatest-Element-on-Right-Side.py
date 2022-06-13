class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            nextMax = max(arr[i:len(arr)])
            arr[i] = nextMax
        del arr[0]
        arr.append(-1)
        return arr