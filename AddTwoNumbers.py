"""
Problem Level: Medium
Understanding the problem #Referred to Youtube
Given -> 2 non-empty linked list with non-negative integers, The digits are stored in reverse order
Return -> Sum of the two numbers represented by the linked list
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            
            carry = val//10
            val = val%10
            
            cur.next = ListNode(val)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next

#example usage
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

sol = Solution()
result = sol.addTwoNumbers(l1, l2)
print(result.val, result.next.val, result.next.next.val) # should print 7, 0, 8
