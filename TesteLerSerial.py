import serial

#ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600,timeout=0)

#ser = serial.Serial(port='COM4',baudrate=9600,timeout=0)

#print("Connected to ttyUSB0");
#print("COM4");

while True:
	ID = ""
	for line in ser.readline():
		#print("Char:" + line)
		
		ID = ID + line
		if(line=="\n"):
			print("Nova linha:" + ID[:-1]);
			ID = ""


ser.close()
