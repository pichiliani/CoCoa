from GPIO import GPIO
from threading import Thread
import sys
import signal
import time
import subprocess
import requests
import serial

THREADS = []

# Classe para lidar com os botoes
class Th(Thread):

		def __init__ (self, num, porta,cb,ser):
			#print("\nMaking thread number " + str(num))
			Thread.__init__(self)
			self.num = num
			self.callback = cb
			self.alive = True
			self.serial = ser
			
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
					self.callback(self.num,self.serial)	
				
				anterior = atual
				time.sleep(0.05)


#Classe para ler da porta serial
class Th_ReadSerial(Thread):

		def __init__ (self, cb):
			
			Thread.__init__(self)
			self.ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600,timeout=0)
			
			print("\n Connected on /dev/ttyUSB0")
			
			self.callback = cb
		
		# Loop principal da thread	
		def run(self):
		
			while True:
				time.sleep(0.05)
				ID = ""
				for line in self.ser.readline():
					#print("Char:" + line)
		
					ID = ID + line
					if(line=="\n"):
						print("Nova ID:" + ID[:-1])
						self.callback(ID[:-1])
						ID = ""
		
		# Envia o caractere pela porta serial	
		def EnviaChar(self,s):
			envia = b''
			envia = envia + s
			
			ser.write(envia);
		
def CallbackLer(x):
	print("Teste de callback")

def MyCallback(x,ser):
	
	# Tocando o audio
	
	# Mandando o comando que liga o led
	if(x==1):
		envia = b''
		envia = envia + "C"
		ser.write(envia)
	if(x==2):
		envia = b''
		envia = envia + "F"
		ser.write(envia)
	if(x==3):
		envia = b''
		envia = envia + "I"
		ser.write(envia)
	if(x==4):
		envia = b''
		envia = envia + "L"
		ser.write(envia)
	if(x==5):
		envia = b''
		envia = envia + "O"
		ser.write(envia)
	if(x==6):
		envia = b''
		envia = envia + "R"
		ser.write(envia)

	time.sleep(0.5)
	print("Botao : " + str(x) + " pressionado!");
	p = subprocess.Popen(['aplay','-D','hw:1,0','assets/audio/' + str(x) + '.wav'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

		
def signal_handler(signal, frame):
	
	for t in THREADS:
		t.alive = False
		t.GPIO.closePin()
	
	thLeSerial.ser.close()
	
	print('Existing the app!')
	sys.exit(0)
	
if __name__ == '__main__':	
	
	#Thread que le os dados da porta serial
	thLeSerial = Th_ReadSerial(CallbackLer)
	thLeSerial.start()	

	# Para lidar com o CTRL+C
	signal.signal(signal.SIGINT, signal_handler)
	
	# Botao 1:  GPIO 36
	thread1 = Th(1,36,MyCallback,thLeSerial.ser)
	thread1.start()
	THREADS.append(thread1)
	
	# Botao 2:  GPIO 13
	thread2 = Th(2,13,MyCallback,thLeSerial.ser)
	thread2.start()
	THREADS.append(thread2)

	# Botao 3:  GPIO 115
	thread3 = Th(3,115,MyCallback,thLeSerial.ser)
	thread3.start()
	THREADS.append(thread3)
	
	# Botao 4:  GPIO 24
	thread4 = Th(4,24,MyCallback,thLeSerial.ser)
	thread4.start()
	THREADS.append(thread4)
	
	# Botao 5:  GPIO 35
	thread5 = Th(5,35,MyCallback,thLeSerial.ser)
	thread5.start()
	THREADS.append(thread5)
	
	# Botao 6:  GPIO 28
	thread6 = Th(6,28,MyCallback,thLeSerial.ser)
	thread6.start()
	THREADS.append(thread6)
	
	while True:
		time.sleep(0.01) # Press Ctrl+c here
