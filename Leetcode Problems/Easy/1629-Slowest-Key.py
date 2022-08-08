'''
A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.

You are given a string keysPressed of length n, where keysPressed[i] was the ith key pressed in the testing sequence, and a sorted list releaseTimes, where releaseTimes[i] was the time the ith key was released. Both arrays are 0-indexed. The 0th key was pressed at the time 0, and every subsequent key was pressed at the exact time the previous key was released.

The tester wants to know the key of the keypress that had the longest duration. The ith keypress had a duration of releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration of releaseTimes[0].

Note that the same key could have been pressed multiple times during the test, and these multiple presses of the same key may not have had the same duration.

Return the key of the keypress that had the longest duration. If there are multiple such keypresses, return the lexicographically largest key of the keypresses.
'''

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxKeyPress = releaseTimes[0]
        outKey = ''
        keyDur = 0
        for i in range(len(keysPressed)):
            
            if(i == 0):
                outKey = keysPressed[0]
                continue
            
            keyDur = releaseTimes[i] - releaseTimes[i - 1]
            if(keyDur > maxKeyPress):
                maxKeyPress = keyDur
                outKey = keysPressed[i]
            
            if(keyDur == maxKeyPress):
                if(keysPressed[i] > outKey):
                    outKey = keysPressed[i]
        
        return outKey   