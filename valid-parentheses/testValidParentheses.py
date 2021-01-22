from validParentheses import Solution

def testValidParentheses(s, expectedOutput):
	print(f'Input - {s}')
	print(f'Output - {Solution().isValid(s)}')
	print(f'Expected - {expectedOutput}')
	print()

testValidParentheses('()', True)
testValidParentheses('()[]{}', True)
testValidParentheses('(]', False)
testValidParentheses('([)]', False)
testValidParentheses('{[]}', True)
testValidParentheses(']', False)
testValidParentheses('(', False)
testValidParentheses('(])', False)
