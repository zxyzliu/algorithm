"""
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents
the position (0-indexed) in the linked list where tail connects to. If pos is -1,
then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Time complexity: Let me denote n as the total number of nodes in the linked list. To analyze its time
complexity, I consider the following two cases separately.
    List has no cycle: The fast pointer reaches the end first and the run time depends on the list's
    length, which is O(n).
    List has a cycle: I break down the movement of the slow pointer into two steps, the non-cyclic part
    and the cyclic part, the worst case time complexity is O(N+K), which is O(n).

Space complexity: O(1). I only use two nodes (slow and fast) so the space complexity is O(1).

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
