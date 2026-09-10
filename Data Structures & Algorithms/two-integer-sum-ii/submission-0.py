class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i in range(length):
            target = float(target) # converting target to float
            if numbers[i] < target / 2: # if num is less than half the target
                indexA = i # save index
                remainder = target - numbers[i]
                for j in range(i+1, length,1):
                    if remainder == numbers[j]:
                        return [(indexA+1), (j+1)]
                    

            