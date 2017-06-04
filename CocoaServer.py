from GPIO import GPIO
from threading import Thread
import sys
import signal
import time
import subprocess
import requests

#NOTA: NaO ESQUECER DE CONFIGURAR ESTE IP_NODEMCU
#NO CODIGO FONTE DO NODEMCU (ARDUINO ESP 8266)
IP_NODEMCU = "192.168.15.32"

THREADS = []

class Th(Thread):

		def __init__ (self, num, porta,cb):
			#print("\nMaking thread number " + str(num))
			Thread.__init__(self)
			self.num = num
			self.callback = cb
			self.alive = True
			
			self.GPIO = GPIO(porta)
			self.GPIO.openPin()
			self.GPIO.setDirection("in")

		# Loop principal da thread	
		def run(self):
			anterior = self.GPIO.getValue()
			
			while (self.alive):
				
				atual = self.GPIO.getValue()
				#print("Valor atual:" + atual)
				#print("Valor anterior:" + anterior)
				
				if atual[:-1] == "0" and anterior[:-1] == "1":
					self.callback(self.num)	
				
				anterior = atual
				time.sleep(0.05)


def MyCallback(x):
	
	# Tocando o audio
	print("Botao : " + str(x) + " pressionado!");
	p = subprocess.Popen(['aplay','-D','hw:1,0','assets/audio/' + str(x) + '.wav'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

	# Mandando o comando que liga o led
	if(x==1):
		requests.get("http://" + IP_NODEMCU + "/C")
	if(x==2):
		requests.get("http://" + IP_NODEMCU + "/F")
	if(x==3):
		requests.get("http://" + IP_NODEMCU + "/I")
	if(x==4):
		requests.get("http://" + IP_NODEMCU + "/L")
	if(x==5):
		requests.get("http://" + IP_NODEMCU + "/O")
	if(x==6):
		requests.get("http://" + IP_NODEMCU + "/R")	
		
def signal_handler(signal, frame):
	
	for t in THREADS:
		t.alive = False
		t.GPIO.closePin()

	print('Existing the app!')
	sys.exit(0)
	
if __name__ == '__main__':	
	signal.signal(signal.SIGINT, signal_handler)

	# Botao 1:  GPIO 36
	thread1 = Th(1,36,MyCallback)
	thread1.start()
	THREADS.append(thread1)
	
	# Botao 2:  GPIO 13
	thread2 = Th(2,13,MyCallback)
	thread2.start()
	THREADS.append(thread2)

	# Botao 3:  GPIO 115
	thread3 = Th(3,115,MyCallback)
	thread3.start()
	THREADS.append(thread3)
	
	# Botao 4:  GPIO 24
	thread4 = Th(4,24,MyCallback)
	thread4.start()
	THREADS.append(thread4)
	
	# Botao 5:  GPIO 35
	thread5 = Th(5,35,MyCallback)
	thread5.start()
	THREADS.append(thread5)
	
	# Botao 6:  GPIO 28
	thread6 = Th(6,28,MyCallback)
	thread6.start()
	THREADS.append(thread6)
	
	while True:
		time.sleep(0.01) # Press Ctrl+c here
