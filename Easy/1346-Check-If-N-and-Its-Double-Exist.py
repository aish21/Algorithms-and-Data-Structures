class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in (arr[:i] + arr[i+1:]):
                if(2*arr[i] == j):
                    return True
        return False