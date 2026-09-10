# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sp = fp = head
        while(True):
            if sp:
                sp = sp.next
            else:
                return False
            if fp and fp.next:
                fp = fp.next.next
            else:
                return False
            
            if(sp == fp):
                break
        return True