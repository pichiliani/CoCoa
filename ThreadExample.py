from threading import Thread
import sys
import signal
import time

COUNTDOWN = 5000

THREADS = []

class Th(Thread):

		def __init__ (self, num,cb):
			#print("\nMaking thread number " + str(num))
			Thread.__init__(self)
			self.num = num
			self.countdown = COUNTDOWN
			self.callback = cb
			self.alive = True

		def run(self):
			while (self.alive):
				#print("\nThread " + str(self.num) + " (" + str(self.countdown) + ")")
				time.sleep(0.01)
				self.countdown -= 1
				self.callback(self.num)


def MyCallback(x):
	print("Dentro do Callback da thread:" + str(x));

def signal_handler(signal, frame):
	
	for t in THREADS:
		t.alive = False

	print('Existing the app!')
	sys.exit(0)
	
if __name__ == '__main__':	
	signal.signal(signal.SIGINT, signal_handler)

	thread = Th(1,MyCallback)
	thread.start()
	THREADS.append(thread)

	thread2 = Th(2,MyCallback)
	thread2.start()
	THREADS.append(thread2)
	
	while True:
		time.sleep(0.01) # Press Ctrl+c here
	
# if __name__ == '__main__':
	# signal.signal(signal.SIGINT, signal_handler)

	# for thread_number in range (5):
			# thread = Th(thread_number,MyCallback)
			# thread.start()

	