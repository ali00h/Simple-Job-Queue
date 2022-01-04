import threading
import time

class sjq(threading.Thread):
	__secondsWait = 0.5
	__jobs = []
	
	def __init__(self,secondsBetweenEachItem = 0.5):
		self.__secondsWait = secondsBetweenEachItem
		threading.Thread.__init__(self)

	def run(self):		
		while True:
			if(len(self.__jobs) > 0):
				item = self.__jobs.pop(0)
				item.handle()
			time.sleep(self.__secondsWait)
	
	def addJob(self,item):
		self.__jobs.append(item)	
