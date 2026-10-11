class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        last = len(nums) -1
        left, right = 0, last
        output = []
        nums.sort()
        

        # Using 2 pointers whist looping through nums
        for i, num in enumerate(nums):
            #Avoid duplicates
            if i > 0 and num == nums[i-1]:
                continue
            left, right = i + 1, last # Decreasing the window of consideration
        
            target = -(nums[i])
            print("target: ", target)
            print("loc: ", i, left, right)

            while left < right:
                curr_sum = nums[left] + nums[right]

                if curr_sum== target:
                    print("found triplet")
                    output.append([nums[left], nums[right], nums[i]])
                    left +=1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    left += 1
        return output
        
        
        
                