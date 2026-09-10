class Solution: 
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict_buffer = {} # initialise dictionary
    for index, num in enumerate(nums): # enumerate keeps track of indexes
      complement = target - num 
      if complement in dict_buffer:
        return [dict_buffer[complement], index]  # Return the indices of the two numbers
      dict_buffer[num] = index  # Store the index of the current number
    return None

        