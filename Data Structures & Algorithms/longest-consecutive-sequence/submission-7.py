class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest = 0

        for n in nums:
            #is n the start?
            if (n-1) not in myset:
                length = 0
                #Check through the set for incrementing values of n
                while (n + length)in myset:
                    length +=1
                    longest = max(length, longest)# Keep track of longest
        
        return longest


            


        


