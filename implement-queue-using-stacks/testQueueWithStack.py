from queueWithStack import MyQueue

def testQueueWithStack(expectedOutput):
	q = MyQueue()
	q.push(1)
	q.push(2)
	print(f'Output - {q.peek()}')
	print(f'Expected - {expectedOutput}\n')
	print(f'Output - {q.peek()}')
	print(f'Expected - {expectedOutput}\n')
	print(f'Output - ' + ('true' if q.empty() else 'false'))
	print(f'Expected - false')

testQueueWithStack(1)
