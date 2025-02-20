class Solution:
    def removeDuplicates(self, nums) -> int:
        j=0
        while(j < len(nums)-1):
            if nums[j] >= nums[j+1]:
                nums.pop(j+1)
            else:
                j+=1
        return len(nums)

#or

class Solution:
    def removeDuplicates(self, nums):
        test=[]
        for num in nums:
            if len(test)>=1 and num == test[-1]:
                continue
            test.append(num)
        i=0
        for m1 in test:
            nums[i] = m1
            i+=1
        nums = nums[:i]
        return len(nums)
