import serial

# Message format in python:
#    [address, ('int', val), ('int long', val), ('char', val), ('string', val), ...]

# Example:
#    msg = [1, ('string', 'eggs&ham'), ('int', 123)]

# Encoded Message Format:
#   {hh (address in hex)}, {h (type byte), h[h[h[h...]]] (data byte(s)}, {more data sections}, '\n'


def arduino():
    def __init__(self, arduinoID, baud, port=None):
        self.arduinoID = arduinoID
        self.ser = serial.Serial(port, baud)

    def findArduinos(self):
        possiblePorts = []

        # Need to look for typical locations here on different platforms
        #if linux:
        #if windows:
        #if osx:

    def setPort(self, port):
        baud = self.ser.baudrate
        self.ser = serial.Serial(port, baud)

    def write(self, msg):
        msgFormatted = self.encode(msg)
        self.ser.write(msgFormatted)

    def rawWrite(self, msg):
        self.ser.write(msg)

    def read(self, timeout):
        msg = self.decode(self.rawRead(timeout))

    def rawRead(self, timeout):
        return self.ser.readline()

    def encode(self, msg):

    def decode(self, msg):

    def dataAvailCallback(self, func):

    
