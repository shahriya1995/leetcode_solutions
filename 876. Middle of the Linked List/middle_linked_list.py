# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # length of linklist
        count = 0
        cur = head
        while cur:
            count = count+1
            cur = cur.next
        print(count)
        #calculate the mid
        if count%2 == 0:
            mid = count //2 + 1
        else:
            mid = count //2 + 1
        print(mid)
        # traverse till you get mid
        k = 0
        cur = head
        while cur:
            k = k+1
            if k == mid:
                return cur
            else:
                cur = cur.next
