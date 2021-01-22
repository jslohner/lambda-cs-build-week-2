class Solution:
	def isValid(self, s: str) -> bool:
		parenChars = {'(': ')', '[': ']', '{': '}'}

		charStack = []

		for i in range(len(s)):
			if s[i] not in parenChars:
				if not charStack:
					return False

				if s[i] == parenChars[charStack[-1]]:
					del charStack[-1]
				else:
					return False

			elif s[i] in parenChars:
				charStack.append(s[i])

		return not charStack
