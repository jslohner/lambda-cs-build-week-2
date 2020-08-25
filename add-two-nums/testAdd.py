from add import ListNode, Solution
import timeit

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
codeTest = '''
Solution().addTwoNumbers(l1, l2)
'''

def testCorrectOutput():
	l3 = Solution().addTwoNumbers(l1, l2)
	output = [int(l3.val)]
	while l3.next:
		output.append(int(l3.next.val))
		l3 = l3.next
	print(f'Input - {[2,4,3]} {[5,6,4]}')
	print(f'Output - {output}')
	print(f'Expected - {[7,0,8]}')

def testLargeNumOfTimes(numTests):
	# numTests = 10000
	time = timeit.timeit(codeTest, number=numTests, globals=globals())
	print(f'addTwoNumbers() ran {numTests} times in {int(time * 1000)} ms')

testCorrectOutput()
testLargeNumOfTimes(10000)
