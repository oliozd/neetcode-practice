class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0  # Start pointer
        right = len(numbers) - 1  # End pointer

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-indexed positions
            elif current_sum < target:
                left += 1  # Move the left pointer to increase the sum
            else:
                right -= 1  # Move the right pointer to decrease the sum
                    

            