from duplicateCheck import Solution

def testCorrectOutput(nums, expectedOutput):
	out = Solution().containsDuplicate(nums)
	print(f'Input - {nums}')
	print(f'Output - ' + ('true' if out else 'false'))
	print(f'Expected - ' + ('true' if expectedOutput else 'false'))
	print()

l1 = [1,2,3,1]
testCorrectOutput(l1, True)
l2 = [1,2,3,4]
testCorrectOutput(l2, False)
l3 = [1,1,1,3,3,4,3,2,4,2]
testCorrectOutput(l3, True)
