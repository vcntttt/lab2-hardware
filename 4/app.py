import wave
import struct
import numpy as np

frecuencias = {
  'Do': 261.63,
  'Re': 293.66,
  'Mi': 329.63,
  'Fa': 349.23,
  'Sol': 392.00,
  'La': 440.00,
  'Si': 493.88,
}

sampleRate1 = 44100 # Usado en 1 y 4
sampleRate2 = 22050
sampleRate3 = 8000
wavsDir = '4/wavs/'

def generateWave(freq, duration, sampleRate):
  t = np.linspace(0, duration, int(sampleRate * duration))
  waveData = np.sin(2 * np.pi * freq * t)
  return waveData


# Ejercicio 1
with wave.open(f'{wavsDir}1-DOREMIFASOLLASI({sampleRate1}Hz).wav', 'w') as waveFile:
  waveFile.setnchannels(1) # Mono
  waveFile.setsampwidth(2) # bytes por muestra
  waveFile.setframerate(sampleRate1)

  for note, freq in frecuencias.items():
    waveData = generateWave(freq, 1, sampleRate1)
    waveDataFinal = [struct.pack('<h', int(sample * 32767)) for sample in waveData]
    waveFile.writeframes(b''.join(waveDataFinal))


# Ejercicio 2
with wave.open(f'{wavsDir}2-SILASOLFAMIREDO({sampleRate2}Hz).wav', 'w') as waveFile:
  waveFile.setnchannels(2) # Stereo
  waveFile.setsampwidth(2)
  waveFile.setframerate(sampleRate2)

  for note, freq in reversed(frecuencias.items()):
    waveData = generateWave(freq, 1, sampleRate2)
    stereoWaveData = [struct.pack('<hh', int(sample * 32767), int(sample * 32767)) for sample in waveData] # hh -> Stereo
    waveFile.writeframes(b''.join(stereoWaveData))


# Ejercicio 3
with wave.open(f'{wavsDir}3-DOREMIFASOLLASI({sampleRate3}Hz).wav', 'w') as waveFile:
  waveFile.setnchannels(1)
  waveFile.setsampwidth(2)
  waveFile.setframerate(sampleRate3)

  for note, freq in frecuencias.items():
    waveData = generateWave(freq, 1, sampleRate3)
    waveDataFinal = [struct.pack('<h', int(sample * 32767)) for sample in waveData]
    waveFile.writeframes(b''.join(waveDataFinal))


# Ejercicio 4
t4 = np.arange(0, 10 * sampleRate1)
wave4 = 8000 * np.sin(2 * np.pi * 500.0 / sampleRate1 * t4) + 8000 * np.sin(2 * np.pi * 250.0 / sampleRate1 * t4)

with wave.open(f'{wavsDir}4-OndaStereo({sampleRate1}Hz).wav', 'w') as waveFile:
  waveFile.setnchannels(2)
  waveFile.setsampwidth(2)
  waveFile.setframerate(sampleRate1)

  waveData = [struct.pack('<hh', int(sample), int(sample)) for sample in wave4]
  waveFile.writeframes(b''.join(waveData))

# Ejercicio 5
def reduceVolume(originalWAV, outputWAV, factor):
  with wave.open(originalWAV, 'r') as originalFile:
    params = originalFile.getparams()
    frames = originalFile.readframes(params.nframes)

    waveData = struct.unpack('<' + 'hh' * params.nframes, frames)

    reducedWaveData = [int(sample * factor) for sample in waveData]

    reducedWaveDataPacked = struct.pack('<' + 'hh' * (len(reducedWaveData) // 2), * reducedWaveData)

  with wave.open(outputWAV, 'w') as reducedFile:
    reducedFile.setparams(params)
    reducedFile.writeframes(reducedWaveDataPacked)

act4File = f'{wavsDir}4-OndaStereo({sampleRate1}Hz).wav'
act5File = f'{wavsDir}5-OndaStereo25%({sampleRate1}Hz).wav'
reduceVolume(act4File, act5File, 0.25)

# Ejercicio 6
with wave.open(act5File, 'r') as reducedFile:
  params = reducedFile.getparams()
  frames = reducedFile.readframes(params.nframes)

  waveData = struct.unpack('<' + 'hh' * params.nframes, frames)
  leftChannel = waveData[0::2]
  rightChannel = waveData[1::2]

with wave.open(f'{wavsDir}6-OndaStereoDerecho({sampleRate1}Hz).wav', 'w') as waveFile:
  waveFile.setparams(params)
  waveFile.writeframes(b''.join([struct.pack('<hh', 0, int(sample)) for sample in rightChannel]))