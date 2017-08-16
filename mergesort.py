# LeetCode 21. Merge Two Sorted Lists
# 8/15/17 - Accepted
# Merge two sorted linked lists and return it as a new list. The new list should be made
# by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        front = ListNode(0)
        new_curr = front
        curr1 = l1
        curr2 = l2

        while True:
            if curr1 == None and curr2 == None:
                break
            elif curr1 and curr2 == None:
                new_curr.next = curr1
                new_curr = new_curr.next
                curr1 = curr1.next
            elif curr1 == None and curr2:
                new_curr.next = curr2
                new_curr = new_curr.next
                curr2 = curr2.next
            elif curr1.val <= curr2.val:
                new_curr.next = curr1
                new_curr = new_curr.next
                curr1 = curr1.next
            elif curr2.val < curr1.val:
                new_curr.next = curr2
                new_curr = new_curr.next
                curr2 = curr2.next

        return front.next



first_1 = ListNode(3)
first_1.next = ListNode(6)
first_2 = first_1.next
first_2.next = ListNode(9)
first_3 = first_2.next

second_1 = ListNode(1)
second_1.next = ListNode(5)
second_2 = second_1.next
second_2.next = ListNode(12)
second_3 = second_2.next

s = Solution()

sol = s.mergeTwoLists(first_1, second_1)

while sol:
    print sol.val
    sol = sol.next