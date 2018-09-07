class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

node1 = Node(9)
node2 = Node(11)
node3 = Node(27)

node1.next = node2
node2.next = node3
node3.next = Node(71)


# runner = node1
# while (runner):
#     if (runner.next.next == None):
#     	runner.next = None
#     runner = runner.next

runner = node1
while (runner):
	print(runner.val)
	runner = runner.next

runner = node1
while (runner):
	if (runner.next.next == None):
		runner.next = None
	runner = runner.next

runner = node1
while (runner):
	print(runner.val)
	runner = runner.next