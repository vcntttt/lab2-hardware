import serial

def sendCommand(command):
    s = serial.Serial('COM2', 9600)
    s.write((command + '\n').encode('utf-8'))
    s.close()

while True:
    command = input("Ingresar comando: ").strip()
    sendCommand(command)
    if command == 'exit': break