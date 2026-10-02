# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = ListNode()
        curr = head
        current_nodes = []

        for i, linked_list in enumerate(lists):
            if linked_list:
                heapq.heappush(current_nodes, (linked_list.val, i, linked_list))

        while current_nodes:
            smallest_val, i, smallest_node = heapq.heappop(current_nodes)

            curr.next = ListNode(smallest_val)
            curr = curr.next

            if smallest_node.next:
                heapq.heappush(current_nodes, (smallest_node.next.val, i, smallest_node.next))

        return head.next
