from reverseInt import Solution

def testReverseInt(x, expectedOutput):
	print(f'Input - {x}')
	print(f'Output - {Solution().reverse(x)}')
	print(f'Expected - {expectedOutput}')
	print()

testReverseInt(12345, 54321)
testReverseInt(-92333, -33329)
testReverseInt(120, 21)
testReverseInt(8463847412, 0)
testReverseInt(-9463847412, 0)
