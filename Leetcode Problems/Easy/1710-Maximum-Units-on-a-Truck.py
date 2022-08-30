'''
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
'''

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse = True)
        boxCount = 0
        output = 0
        for i in range(len(boxTypes)):
            if(boxCount + boxTypes[i][0] < truckSize):
                output += (boxTypes[i][0] * boxTypes[i][1])
                boxCount += boxTypes[i][0]
            else:
                totalToBeUsed = truckSize - boxCount
                output += (totalToBeUsed * boxTypes[i][1])
                break
        return output