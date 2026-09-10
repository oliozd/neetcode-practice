class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        prefix_arr = [0] * len(nums)
        postfix_arr = [0] * len(nums)
        output = [0]* len(nums)
        result = 1
        for i in range(len(nums)):
            result = nums[i] * result
            prefix_arr[i] = result
        
        result = 1
        for i in range(len(nums)-1, -1,  -1):
            result = nums[i] * result
            postfix_arr[i] = result
        
        for  num in range(len(nums)):
            if num == 0:
                print(num)
                output[num] = (1* (postfix_arr[num+1]))
            elif num == (len(nums)-1):
                output[num] = (prefix_arr[num-1])* 1
            else:
                output[num] = (prefix_arr[num-1])* (postfix_arr[num+1])
        return output



