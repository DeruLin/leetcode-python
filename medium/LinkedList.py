# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add = 0
        temp = l1.val + l2.val
        if temp > 9:
            add = 1
            temp -= 10
        result = ListNode(temp)
        current_node = result
        while l1.next is not None and l2.next is not None:
            l1 = l1.next
            l2 = l2.next
            temp = l1.val + l2.val + add
            if temp > 9:
                add = 1
                temp -= 10
            else:
                add = 0
            current_node.next = ListNode(temp)
            current_node = current_node.next
        while l1.next is not None:
            l1 = l1.next
            temp = l1.val + add
            if temp > 9:
                add = 1
                temp -= 10
            else:
                add = 0
            current_node.next = ListNode(temp)
            current_node = current_node.next
        while l2.next is not None:
            l2 = l2.next
            temp = l2.val + add
            if temp > 9:
                add = 1
                temp -= 10
            else:
                add = 0
            current_node.next = ListNode(temp)
            current_node = current_node.next
        if add == 1:
            current_node.next = ListNode(1)
        return result


if __name__ == "__main__":
    nums = [5, 1, 5, 5, 2, 5, 4]
    print(Solution().addTwoNumbers(nums))
