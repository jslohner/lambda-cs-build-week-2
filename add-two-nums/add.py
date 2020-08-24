# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		return f'ListNode{{val: {self.val}, next: {self.next}}}'

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		# numList1 = [l1.val]
		# numList2 = [l2.val]
		# while l1.next:
		#     numList1.append(l1.next.val)
		#     l1 = l1.next
		# while l2.next:
		#     numList2.append(l2.next.val)
		#     l2 = l2.next
		# num1 = ''
		# num2 = ''
		# for n in reversed(numList1):
		#     num1 += str(n)
		# for n in reversed(numList2):
		#     num2 += str(n)
		# ansStr = str(int(num1) + int(num2))
		# ansList = []
		# for i in range((len(ansStr) - 1), -1, -1):
		#     ansList.append(ansStr[i])
		# idx = 1
		# l3 = ListNode(ansList[0])
		# current = l3
		# while idx < len(ansStr):
		#     current.next = ListNode(ansList[idx])
		#     current = current.next
		#     idx += 1
		# return l3

		numList1 = [l1.val]
		numList2 = [l2.val]
		while l1.next:
			numList1.append(l1.next.val)
			l1 = l1.next
		while l2.next:
			numList2.append(l2.next.val)
			l2 = l2.next
		x = list(str(int(''.join([str(n) for n in numList1[::-1]])) + int(''.join([str(n) for n in numList2[::-1]]))))[::-1]
		idx = 0
		l3 = ListNode(x[0])
		current = l3
		while idx < (len(x) - 1):
			current.val = x[idx]
			current.next = ListNode(x[idx + 1])
			current = current.next
			idx += 1
		return l3

		# idx = 1
		# l3 = ListNode(x[0])
		# current = l3
		# while idx < len(x):
		#     current.next = ListNode(x[idx])
		#     current = current.next
		#     idx += 1
		# return l3
