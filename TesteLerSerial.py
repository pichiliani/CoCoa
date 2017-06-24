import serial

ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600,timeout=0)

#ser = serial.Serial(port='COM4',baudrate=9600,timeout=0)

#print("Connected to ttyUSB0");
#print("COM4");

while True:
	ID = ""
	for line in ser.readline():
		#print("Char:" + chr(line))
		#print(line)

		ID = ID + chr(line)
		if(line==10):
			print("Nova linha:" + ID[:-1]);
			ID = ""


ser.close()
