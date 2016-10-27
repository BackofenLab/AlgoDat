import timeit
import random

def init(size):
	# use system time as seed
	random.seed(None)
	
	# set linear order as accessor
	order = [a for a in range(0, size)]
	
	# init array with random data
	data = [random.random() for a in order]
	
	return (order, data)

def test(array):
	# retrieve data
	(order, data) = array
	
	# init the sum value
	s = 0
	
	for index in order:
		s += data[index]
	
	return s

with open('cache_linear_runtime.csv', 'w') as f:
	f.write("x;y\n")
	for m in range(0, 100):
		m = m * 1000
		result = ('%d;%.6f\n' % (m, timeit.timeit('test(a)', setup='from __main__ import init,test\na=init(' + str(m) + ')', number=5))).replace('.', ',')
		print(result)
		f.write(result)
