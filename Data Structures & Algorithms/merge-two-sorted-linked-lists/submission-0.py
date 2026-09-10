# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        
        if not list2:
            return list1

        
        # Dummy node
        h_node = p_node = ListNode()

        while(list1 and list2):
            if list1.val <= list2.val:
                p_node.next = list1
                list1 = list1.next # Increment
            else:
                p_node.next = list2
                list2 = list2.next # Increment
            p_node= p_node.next
        #Sorting out uneven lists:
        if list1:
            p_node.next = list1
        if list2:
            p_node.next = list2
        return h_node.next
        

        