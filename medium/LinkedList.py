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

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 2
        if head is None or head.next is None:
            return head
        odd_head = head
        odd_temp = odd_head
        even_head = head.next
        even_temp = even_head
        head = head.next
        even_count = 0
        while head.next is not None:
            head = head.next
            count += 1
            if count % 2 == 0:
                even_count += 1
                even_temp.next = head
                even_temp = even_temp.next
            else:
                odd_temp.next = head
                odd_temp = odd_temp.next
        even_temp.next = None
        odd_temp.next = even_head
        return odd_head

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        temp_head_a = headA
        length_a = 0
        temp_head_b = headB
        length_b = 0
        while temp_head_a.next is not None:
            temp_head_a = temp_head_a.next
            length_a += 1
        while temp_head_b.next is not None:
            temp_head_b = temp_head_b.next
            length_b += 1
        if temp_head_a is not temp_head_b:
            return None
        if length_a > length_b:
            step = length_a - length_b
            for i in range(step):
                headA = headA.next
            while headA is not headB:
                headA = headA.next
                headB = headB.next
        else:
            step = length_b - length_a
            for i in range(step):
                headB = headB.next
            while headA is not headB:
                headA = headA.next
                headB = headB.next
        return headA


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(Solution().oddEvenList(head))
