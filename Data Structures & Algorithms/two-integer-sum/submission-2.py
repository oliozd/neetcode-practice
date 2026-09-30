class Solution: 
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    nummap: dict[int, int] = {}

    for i, n1 in enumerate(nums):
      
      n2 = target - n1
     
      if n2 in nummap:
        return [nummap[n2], i]
      else:
        nummap[n1] = i
      
    return []
        