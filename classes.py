# classes

#queue
class SuperQueue:

	def __init__(self, dim):
		self.items = []
		self.dim = dim
	
	def put(self, el):
		if len(self.items) == self.dim:
			self.items = self.items[1 :]
		self.items.append(el)
		
	def clear(self):
		del self.items[:]
		self.dim = 0
		
	def changeSize(self, dim):
		self.dim = dim
		
	def show(self):
		print(self.items)

# container for tuples
class TuplesContainer:

	def __init__(self):
		self.x = []
		self.y = []
		
	def put(self, x, y):
		self.x.append(x)
		self.y.append(y)

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y