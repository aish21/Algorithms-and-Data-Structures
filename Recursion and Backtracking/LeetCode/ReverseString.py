def ReverseString(s):
    start = 0
    end = len(s) - 1

    while(start < end):
        temp = s[start]
        s[start] = s[end]
        s[end] = temp

        start += 1
        end -= 1
    
    print(s)

userInp = input('Enter String:\n')
ReverseString(list(userInp))
