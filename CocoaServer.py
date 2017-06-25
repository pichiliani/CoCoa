from GPIO import GPIO
from threading import Thread
import sys
import signal
import time
import subprocess
import requests
import serial
from twx.botapi import TelegramBot

THREADS = []

ADADOS = []


# Classe para lidar com os leds da DrabonBoard
class ThLedDragon(Thread):

		def __init__ (self, num, porta):
			Thread.__init__(self)
			self.num = num
			
			self.GPIO = GPIO(porta)
			self.GPIO.openPin()
			self.GPIO.setDirection("out")

		# Loop principal da thread	
		def run(self):
			self.GPIO.setValue(1)
			time.sleep(.2)
			self.GPIO.setValue(0)
			time.sleep(.2)
			self.GPIO.setValue(1)
			time.sleep(.2)
			self.GPIO.setValue(0)
			time.sleep(.2)
			self.GPIO.setValue(1)
			time.sleep(.2)
			self.GPIO.setValue(0)
			
			self.GPIO.closePin()

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
		
					ID = ID + chr(line)
					if(line==10):
						print("Nova ID:" + ID[:-2])
						self.callback(ID[:-2])
						ID = ""
		
		# Envia o caractere pela porta serial	
		def EnviaChar(self,s):
			envia = b''
			envia = envia + s
			
			ser.write(envia);
		

#Classe para enviar mensagem para o Telegram
class Th_BotTelegram(Thread):

		def __init__ (self, bot, msg):
			
			Thread.__init__(self)
			self.botTelegram = bot
			self.mensagem = msg
			
			print("\n Connected on /dev/ttyUSB0")
		
		# Loop principal da thread	
		def run(self):
			# Enviando a mensagem o Mauro e a Talita
			
			#Mauro
			user_id1 = int(315613935)
			result = self.botTelegram.send_message(user_id1, 'Rafael diz: '+self.mensagem).wait()

			#Talita
			user_id2 = int(114793889)
			result = self.botTelegram.send_message(user_id2, 'Rafael:' + self.mensagem).wait()

def CallbackLer(x):
	print("Teste de callback")

def AcionaBotaoCallback(x,ser):
	
	# Piscando o LED
	envia = b''
	
	if(x==1): 
		envia = envia + ADADOS[0][3] # Piscar

	if(x==3): 
		envia = envia + ADADOS[1][3] # Piscar
	
	if(x==4): 
		envia = envia + ADADOS[2][3] # Piscar
	
	if(x==6): 
		envia = envia + ADADOS[3][3] # Piscar
	
	ser.write(envia)
	
	
	arquivo = ADADOS[x-1][0]
	time.sleep(0.5)
	
	
	# Tocando o audio
	print("Botao : " + str(x) + " pressionado!");
	p = subprocess.Popen(['aplay','-D','hw:1,0','assets/audio/' + arquivo],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	
		
	# Leds da DrabonBoard
#	if(x==2):
#		th = ThLedDragon(5,12)
#		th.start()
		
#	if(x==5):
#		th = ThLedDragon(6,69)
#		th.start()
		
	# Enviando a mensagem para o bot
	thBot = Th_BotTelegram(bot, ADADOS[x-1][5])
	thBot.start()
		
def signal_handler(signal, frame):
	
	for t in THREADS:
		t.alive = False
		t.GPIO.closePin()
	
	thLeSerial.ser.close()
	
	print('Existing the app!')
	sys.exit(0)

# Inicializa a ThreadSerial
def loadThreadSerial():
	thLeSerial = Th_ReadSerial(CallbackLer)
	thLeSerial.start()

	return thLeSerial

# Inicializa os botoes	
def loadButtons(thLeSerial):
	# Botao 1:  GPIO 36
	thread1 = Th(1,36,AcionaBotaoCallback,thLeSerial.ser)
	thread1.start()
	THREADS.append(thread1)
	
	# Botao 2:  GPIO 13
	thread2 = Th(2,13,AcionaBotaoCallback,thLeSerial.ser)
	thread2.start()
	THREADS.append(thread2)

	# Botao 3:  GPIO 115
	thread3 = Th(3,115,AcionaBotaoCallback,thLeSerial.ser)
	thread3.start()
	THREADS.append(thread3)
	
	# Botao 4:  GPIO 24
	thread4 = Th(4,24,AcionaBotaoCallback,thLeSerial.ser)
	thread4.start()
	THREADS.append(thread4)
	
	# Botao 5:  GPIO 35
	thread5 = Th(5,35,AcionaBotaoCallback,thLeSerial.ser)
	thread5.start()
	THREADS.append(thread5)
	
	# Botao 6:  GPIO 28
	thread6 = Th(6,28,AcionaBotaoCallback,thLeSerial.ser)
	thread6.start()
	THREADS.append(thread6)

# Inicializa os botoes	
def loadData():
	
	# BOTAO 1
	x = []
	x.append("1.wav") # Arquivo
	x.append(b"A") # Comando para acender o led
	x.append(b"B") # Comando para apagar o led
	x.append(b"C") # Comando para piscar o led
	x.append("697E6F3B") # ID do RFID
	x.append("Estou com fome") # Mensagem para boot
	
	ADADOS.append(x)
	
	# BOTAO 2
	x = []
	x.append("2.wav") # Arquivo
	x.append(b"D") # Comando para acender o led
	x.append(b"E") # Comando para apagar o led
	x.append(b"F") # Comando para piscar o led
	x.append("DD9DDAAB") # ID do RFID
	x.append("Estou com sede") # Mensagem para boot
	
	ADADOS.append(x)
	
	# BOTAO 3
	x = []
	x.append("3.wav") # Arquivo
	x.append(b"G") # Comando para acender o led
	x.append(b"H") # Comando para apagar o led
	x.append(b"I") # Comando para piscar o led
	x.append("F0A5DBAB") # ID do RFID
	x.append("Estou com dor") # Mensagem para boot
	
	ADADOS.append(x)
	
	# BOTAO 4
	x = []
	x.append("4.wav") # Arquivo
	x.append(b"J") # Comando para acender o led
	x.append(b"K") # Comando para apagar o led
	x.append(b"L") # Comando para piscar o led
	x.append("722B725B") # ID do RFID
	x.append("Estou com sono") # Mensagem para boot
	
	ADADOS.append(x)
	
	# BOTAO 5
	x = []
	x.append("5.wav") # Arquivo
	x.append(b"M") # Comando para acender o led
	x.append(b"N") # Comando para apagar o led
	x.append(b"O") # Comando para piscar o led
	x.append("6A731085") # ID do RFID
	x.append("Quero ir ao banheiro") # Mensagem para boot
	
	ADADOS.append(x)
	
	# BOTAO 6
	x = []
	x.append("6.wav") # Arquivo
	x.append(b"P") # Comando para acender o led
	x.append(b"Q") # Comando para apagar o led
	x.append(b"R") # Comando para piscar o led
	x.append("6A731085") # ID do RFID
	x.append("Preciso de ajuda") # Mensagem para boot
	
	ADADOS.append(x)

	# BOTAO 7
	x = []
	x.append("7.wav") # Arquivo
	x.append(b"") # Comando para acender o led
	x.append(b"") # Comando para apagar o led
	x.append(b"") # Comando para piscar o led
	x.append("C7824439") # ID do RFID
	x.append("Preciso de ajuda") # Mensagem para boot
	
	ADADOS.append(x)
	
	# BOTAO 8
	x = []
	x.append("8.wav") # Arquivo
	x.append(b"") # Comando para acender o led
	x.append(b"") # Comando para apagar o led
	x.append(b"") # Comando para piscar o led
	x.append("1A76D5AB") # ID do RFID
	x.append("O barulho me incomoda") # Mensagem para boot
	
	ADADOS.append(x)
	
# Inicializa os botoes	
def loadThreadTelegram():
	# Carregando o bot no TelegramBot
	bot = TelegramBot('438194506:AAGYIHrARnrnVU1Ev9UOrYA7hdvOXFW0g-Y')	
	
	return bot
	
		
# Ponto de entrada principal	
if __name__ == '__main__':	
	
	# Para lidar com o CTRL+C
	signal.signal(signal.SIGINT, signal_handler)
	
	#Carregando a Thread the vai se comunicar com o bot
	bot = loadThreadTelegram()
	
	#Thread que le os dados da porta serial
	thLeSerial = loadThreadSerial()
	
	# Carregando os botoes
	loadButtons(thLeSerial)
	
	# Carregando os dados de audio e info
	loadData()
	
	while True:
		time.sleep(0.01) # Press Ctrl+c here
