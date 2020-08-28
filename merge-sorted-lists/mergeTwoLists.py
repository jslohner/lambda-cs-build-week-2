class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		return f'{self.val} -> {self.next}'

class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if (not l1) and (not l2):
			return None
		nodes = []
		c = l1
		while c:
			nodes.append(c.val)
			c = c.next
		c = l2
		while c:
			nodes.append(c.val)
			c = c.next
		nodes = sorted(nodes)
		l3 = ListNode()
		c = l3
		idx = 0
		while idx < len(nodes):
			c.val = nodes[idx]
			if not (idx + 1 >= len(nodes)):
				c.next = ListNode(nodes[idx + 1])
			c = c.next
			idx += 1
		return l3
