import win32api, win32con, serial

keysMap = {
    'play': 0xB3,
    'stop': 0xB2,
    'volUp' : 0xAF,
    'volDown' : 0xAE,
    'next': 0xB0,
    'prev': 0xB1,
    'pause': 0xB3,
}

def pressKey(keyCode):
    win32api.keybd_event(keyCode, 0, 0, 0)
    win32api.keybd_event(keyCode, 0, win32con.KEYEVENTF_KEYUP, 0)

def controlMediaPlayer(action):
    if action in keysMap:
        pressKey(keysMap[action])
        print(f"{action} presionado")
    else:
        print(f"Accion desconocida: {action}")

def startServer():
    try:
        s = serial.Serial('COM2', 9600)
        print("Server iniciado")
    except serial.SerialException as error:
        print(f"Error al iniciar el servidor {error}")
        return
    
    while True:
        if s.in_waiting > 0:
            action = s.readline().decode('utf-8').strip()
            if action == 'exit':
                break
            controlMediaPlayer(action)

startServer()