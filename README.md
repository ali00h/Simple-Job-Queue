# Simple Job Queue
`SJQ` is a simple Python library for queueing jobs and processing them in the background with threading. This does not require any cache database like `Redis` or `File System`.

# How to use
All processing items should be an instance of a class that has a handle method. For example:

```python
class foo:
	x=0
	
	def __init__(self,val):
		self.x = val
	
	def handle(self):
		print("In foo: x=" + str(self.x))
```

You can create queue by creating an instance of `sjq` class. You can define seconds between each item processing. It's optional and default value is 0.5 second. For starting proccessing items, you should call `start` method. If you want to add new item to queue, you can use `addJob` method. 

```python
a = sjq(2)
a.start()
try:
	for x in range(10):
		fooObj = foo(x)
		a.addJob(fooObj)
		time.sleep(1)
except KeyboardInterrupt:
	a.join()	
```
