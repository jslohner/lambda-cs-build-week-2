from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		mem = {}
		for i in range(len(nums)):
			if nums[i] not in mem:
				mem[nums[i]] = []
			mem[nums[i]].append(i)

		for key, val in mem.items():
			diff = target - key
			if (diff in mem):
				if (diff == key):
					if len(val) > 1:
						return val
				else:
					return [mem[key][0], mem[diff][0]]
