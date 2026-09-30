class Solution: 
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    # Hashmap solution(O(n) space)
    """
    nummap: dict[int, int] = {}

    for i, n1 in enumerate(nums):
      
      n2 = target - n1
     
      if n2 in nummap:
        return [nummap[n2], i]
      else:
        nummap[n1] = i
      
    return []

    """
    # Two pointer solution

    i_t = []
    for i, num in enumerate(nums):
      i_t.append([num, i])

    i_t.sort()

    p1 = 0
    p2 = len(nums) -1
    target = target
    while p1 < p2:

      curr = i_t[p1][0] + i_t[p2][0] # Accessing the nums each time
      curr = curr
      print(f"{i_t[p1][0]} + {i_t[p2][0]} = {curr}")
      if target == curr:
        return [min(i_t[p1][1], i_t[p2][1]), max(i_t[p2][1], i_t[p1][1])] # Return the smaller of the index first and larger second(as per requirement)
      
      elif target > curr:
        p1 += 1
      
      elif target < curr:
        p2 -= 1
    
    return []



        