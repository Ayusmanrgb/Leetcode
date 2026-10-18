class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            
            curr.next = ListNode(total_sum % 10)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy_head.next
