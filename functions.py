import classes

# functions

def getAvg(array):

	sum = 0
	
	for el in array:
		sum = sum + el
		
	return sum / len(array)
	
# returns the weighted average for a queue
def getWeightedFloatingAvg(queue, len):

	fibo = 0
	sum = 0
	size = len
		
	for k in queue.items:
		fibo += size
		sum += (len - size + 1) * k
		size -= 1
		
	return (sum / fibo)

# returns the peaks in the series
def getMaxes(array):

	maxes = classes.TuplesContainer()

	if(len(array) != 0):
		max = array[0]
		prev = array[0]

		for i in range(0, len(array)-1):
			item = array[i]
			if item > prev and item > array[i+1]:
				maxes.put(i, item)
			prev = item
	
	return maxes

# returns the lows in the series
def getMins(array):

	mins = classes.TuplesContainer()

	if(len(array) != 0):
		min = array[0]
		prev = array[0]

		for i in range(0, len(array)-1):
			item = array[i]
			if item < prev and item < array[i+1]:
				mins.put(i, item)
			prev = item
	
	return mins