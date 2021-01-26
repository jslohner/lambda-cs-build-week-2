from romanToInt import Solution

def testRomanToInt(s, expectedOutput):
	print(f'Input - {s}')
	print(f'Output - {Solution().romanToInt(s)}')
	print(f'Expected - {expectedOutput}')
	print()

testRomanToInt('III', 3)
testRomanToInt('IV', 4)
testRomanToInt('IX', 9)
testRomanToInt('LVIII', 58)
testRomanToInt('MCMXCIV', 1994)
testRomanToInt('MMCCCLXIX', 2369)
testRomanToInt('MMMCCCXXXIII', 3333)
testRomanToInt('MMMCDXX', 3420)
