class MyQueue:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.q = []

	def push(self, x: int) -> None:
		"""
		Push element x to the back of queue.
		"""
		self.q.append(x)

	def pop(self) -> int:
		"""
		Removes the element from in front of queue and returns that element.
		"""
		# x = self.q[0]
		# del self.q[0]
		# return x
		return self.q.pop(0)

	def peek(self) -> int:
		"""
		Get the front element.
		"""
		return self.q[0]

	def empty(self) -> bool:
		"""
		Returns whether the queue is empty.
		"""
		return len(self.q) == 0
