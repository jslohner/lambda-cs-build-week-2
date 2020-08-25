from twoSum import Solution

def testTwoSum(nums, target, expectedOutput):
	print(f'Input - {nums} | {target}')
	print(f'Output - {Solution().twoSum(nums, target)}')
	print(f'Expected - {expectedOutput}')
	print()

testTwoSum([2, 7, 11, 15], 9, [0, 1])
testTwoSum([1, 4, 8, 9, 13, 15], 17, [1, 4])
testTwoSum([3, 4, 8, 9, 20, 23, 27, 33, 38, 41, 43, 44, 50], 60, [6, 7])
