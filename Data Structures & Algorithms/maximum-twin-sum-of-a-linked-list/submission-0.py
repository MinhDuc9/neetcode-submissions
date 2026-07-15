# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # first half
        slow = fast = head
        behind = None

        # find middle, and reverse
        while fast != None and fast.next != None:
            fast = fast.next.next

            curr = slow
            slow = slow.next
            curr.next = behind
            behind = curr


        firstPair = curr
        secondPair = slow
        res = 0
        
        while firstPair != None:
            res = max(res, firstPair.val + secondPair.val)
            firstPair = firstPair.next
            secondPair = secondPair.next

        return res
