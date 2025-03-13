class Solution:
    def reverse(self,x):
        reverseNum=0
        isNegative= False

        if x < 0:
            isNegative = True
            x = x * (-1)

        while x>0:
            lastNum=x%10
            x=x//10
            reverseNum=(reverseNum*10)+lastNum

        if isNegative == True:
            reverseNum = reverseNum*-1

        INT_MAX = 2**31 - 1  # Maximum value for a signed 32-bit integer
        INT_MIN = -2**31 

        if reverseNum>INT_MAX or reverseNum<INT_MIN:
            return 0

        return reverseNum
    
