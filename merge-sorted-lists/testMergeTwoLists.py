from mergeTwoLists import ListNode, Solution
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
def testMergeTwoLists(l1: ListNode, l2: ListNode, expectedOutput: ListNode) -> ListNode:
	print(f'Input - ({l1}) | ({l2})')
	print(f'Output - ({Solution().mergeTwoLists(l1, l2)})')
	print(f'Expected - ({expectedOutput})')

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
expectedOutput = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
testMergeTwoLists(l1, l2, expectedOutput)
