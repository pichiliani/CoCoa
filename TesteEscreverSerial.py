import serial

#ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600,timeout=0)

ser = serial.Serial(port='COM4',baudrate=9600,timeout=0)

#print("Connected to ttyUSB0");
print("Connected to COM4");


ser.write(b"C");

ser.close()
