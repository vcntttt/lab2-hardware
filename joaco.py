import wave
import struct
import numpy as np

# Escala Musical Pentatónica: Do, Re, Mi, Fa, Sol, La y Si, a una tasa de sampleo de 44.100 en Mono.
Escala_pentatonica = {
    'Do': 261.63,
    'Re': 293.66,
    'Mi': 329.63,
    'Fa': 349.23,
    'Sol': 392.00,
    'La': 440.00,
    'Si': 493.88    
}
duracion = 0.14285714285
tasa_de_sampleo = 44100

def generar_sonido(frecuencia, duracion, tasa_de_sampleo):
    muestras = []
    n_muestras = int(duracion * tasa_de_sampleo)
    for i in range(n_muestras):
        muestra = int(10000 * np.sin(2 * np.pi * frecuencia * i / tasa_de_sampleo))
        muestras.append(muestra)
    return muestras


with wave.open('Escala Musical Pentatónica1.wav', 'w') as wav_file:   
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(tasa_de_sampleo)
    wav_file.setcomptype('NONE', 'Not Compressed')

    for nota in Escala_pentatonica:
        frecuencia = Escala_pentatonica[nota]
        muestras = generar_sonido(frecuencia, duracion,tasa_de_sampleo)
        datos_bytes = b''

        for muestra in muestras:
            datos_bytes += struct.pack('<h', muestra)

        wav_file.writeframesraw(datos_bytes)

# Escala Musical Pentatónica: Si, La, Sol, Fa, Mi, Re y Do, a una tasa de sampleo de 22.050 en Stereo.
Escala_pentatonica2 = {
    'Si': 493.88,
    'La': 440.00,
    'Sol': 392.00,
    'Fa': 349.23,
    'Mi': 329.63,
    'Re': 293.66,
    'Do': 261.63,
}
tasa_de_sampleo2 = 22050
duracion2 = duracion * 2

with wave.open('Escala Musical Pentatónica2.wav', 'w') as wav_file:   
    wav_file.setnchannels(2)  # Stereo
    wav_file.setsampwidth(2)
    wav_file.setframerate(tasa_de_sampleo2)
    wav_file.setcomptype('NONE', 'Not Compressed')

    for nota2 in Escala_pentatonica2:
        frecuencia2 = Escala_pentatonica2[nota2]
        muestras2 = generar_sonido(frecuencia2, duracion2, tasa_de_sampleo2)
        datos_bytes2 = b''

        for muestra2 in muestras2:
            datos_bytes2 += struct.pack('<h', muestra2)

        wav_file.writeframesraw(datos_bytes2)

#Escala Musical Pentatónica: Do, Re, Mi, Fa, Sol, La y Si, a una tasa de sampleo de 8.000 en Mono.
tasa_de_sampleo3 = 8000
with wave.open('Escala Musical Pentatónica3.wav', 'w') as wav_file:   
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(tasa_de_sampleo3)
    wav_file.setcomptype('NONE', 'Not Compressed')

    for nota in Escala_pentatonica:
        frecuencia = Escala_pentatonica[nota]
        muestras = generar_sonido(frecuencia, duracion, tasa_de_sampleo3)
        datos_bytes = b''

        for muestra in muestras:
            datos_bytes += struct.pack('<h', muestra)

        wav_file.writeframesraw(datos_bytes)

#Genere la siguiente onda en stereo (RATE=44.100) durante 10s y visualice con Audacity:
#y = 8.000*sin(2*pi*500.0/RATE*i) + 8.000*sin(2*pi*250.0/RATE*i), i = 0,1,.. RATE

RATE = 44100
duracion3 = 10

def generar_onda(duracion, RATE):
    muestras = []
    n_muestras = int(duracion * RATE)
    for i in range(n_muestras):
        y = int(8000*np.sin(2*np.pi*500.0/RATE*i) + 8000*np.sin(2*np.pi*250.0/RATE*i))
        muestras.append(y)
        muestras.append(y)
    return muestras

muestras = generar_onda(duracion3, RATE)

with wave.open('Onda Stereo.wav', 'w') as wav_file:   
    wav_file.setnchannels(2)
    wav_file.setsampwidth(2)
    wav_file.setframerate(RATE)
    wav_file.setcomptype('NONE', 'Not Compressed')

    for muestra in muestras:
        wav_file.writeframesraw(struct.pack('<h', muestra))

#Baje el volumen de la onda anterior en un 75% utilizando Python.

def generar_onda_menor(duracion, RATE):
    muestras = []
    n_muestras = int(duracion * RATE)
    for i in range(n_muestras):
        y = int(8000*np.sin(2*np.pi*500.0/RATE*i) + 8000*np.sin(2*np.pi*250.0/RATE*i)* 0.25)
        muestras.append(y)
        muestras.append(y)
    return muestras

muestras = generar_onda_menor(duracion3, RATE)

with wave.open('Onda Stereo de 75% menos.wav', 'w') as wav_file:   
    wav_file.setnchannels(2)
    wav_file.setsampwidth(2)
    wav_file.setframerate(RATE)
    wav_file.setcomptype('NONE', 'Not Compressed')

    for muestra in muestras:
        wav_file.writeframesraw(struct.pack('<h', muestra))

#Limpie el canal izquierdo de la señal anterior con Python y reproduzca con Audacity.

def generar_onda_menor(duracion, RATE):
    muestras = []
    n_muestras = int(duracion * RATE)
    for i in range(n_muestras):
        y = int(8000*np.sin(2*np.pi*500.0/RATE*i) + 8000*np.sin(2*np.pi*250.0/RATE*i)* 0.25)
        muestras.append([y,y])
    return muestras

muestras = generar_onda_menor(duracion3, RATE)

muestras_modificadas = [(0, y_derecho) for y_izquierdo, y_derecho in muestras]

with wave.open('Onda Stereo Canal Izquierdo Limpio.wav', 'w') as wav_file:
    wav_file.setnchannels(2)
    wav_file.setsampwidth(2)
    wav_file.setframerate(RATE)
    wav_file.setcomptype('NONE', 'Not Compressed')

    for muestra_izq, muestra_der in muestras_modificadas:
        wav_file.writeframes(struct.pack('<hh', muestra_izq, muestra_der))
