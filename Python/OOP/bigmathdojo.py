class MathDojo:
	def __init__(self):
		self.total = 0
		result = 0

	def add(self,num1, *nums):
		self.total = num1
		# print("****", self.total)

		for x in nums:
			self.total += x
			#print(x)

		return self.total


md = MathDojo()
md.add(2)	
print(md.add(2))
print(md.add(3,5,8,2))


