import time
from sjq import sjq

class foo:
	x=0
	
	def __init__(self,val):
		self.x = val
	
	def handle(self):
		print("In foo: x=" + str(self.x))

	
if(__name__ == '__main__'):
	a = sjq(2)
	a.start()

	for x in range(10):
		fooObj = foo(x)
		a.addJob(fooObj)
		time.sleep(1)

