# LeetCode 2. Add Two Numbers
# 8/11/17 - accepted
# You are given two non-empty linked lists representing two non-negative integers. The digits
# are stored in reverse order and each of their nodes contain a single digit. Add the two
# numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        front = ListNode(0)
        current = front

        a = l1
        b = l2
        carry = 0

        while a or b:
            if a == None:
                x = 0
            else:
                x = a.val

            if b == None:
                y = 0
            else:
                y = b.val

            sum = carry + x + y
            carry = sum / 10
            current.next = ListNode(sum % 10)

            current = current.next

            if a != None:
                a = a.next

            if b != None:
                b = b.next

        if carry > 0:
            current.next = ListNode(carry)

        return front.next

first_1 = ListNode(2)
first_1.next = ListNode(4)
first_2 = first_1.next
first_2.next = ListNode(3)
first_3 = first_2.next

second_1 = ListNode(5)
second_1.next = ListNode(6)
second_2 = second_1.next
second_2.next = ListNode(4)
second_3 = second_2.next

sol = Solution()
ok = sol.addTwoNumbers(first_1, second_1)

while ok:
    print ok.val
    ok = ok.next