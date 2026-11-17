# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1. find the end of the list (where next == None)
        #2. set the next value in rev to the new val, and append the new node with next as None
        #3. set next on the current node to None
        #4. repeat until head.next == None

        cur = head
        out = None
        if head:
            while head.next != None:
                cur = head
                while cur.next.next != None:
                    cur = cur.next
                if out == None:
                    out = ListNode(cur.next.val, None)
                    pos = out
                    cur.next = None
                else:
                    pos.next = ListNode(cur.next.val, None)
                    pos = pos.next
                    cur.next = None
                print(pos.val)
            if out != None:
                pos.next = ListNode(head.val, None)
            else:
                out = ListNode(head.val, None)
            return out
        return