import numpy as np, matplotlib.pyplot as plt

FREQ_0= 1000
FREQ_1 = 50
SAMPLE = 44100
S_RATE = 44100.0

s_1 = [np.sin(2*np.pi * FREQ_0 * i/S_RATE) for i in range(SAMPLE)]
s_2 = [np.sin(2*np.pi * FREQ_1 * i/S_RATE) for i in range(SAMPLE)]
w_1 = np.array(s_1); w_2 = np.array(s_2)
w12 = w_1 + w_2

fft_s1 = np.fft.fft(w_1)
fft_s2 = np.fft.fft(w_2)
fft_w12 = np.fft.fft(w12)

freqs = np.fft.fftfreq(SAMPLE, 1/S_RATE)

plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(w_1)
plt.ylim(-1, 1)
plt.xlim(0, 500)
plt.title('Onda Original')

plt.subplot(4, 1, 2)
plt.plot(w_2)
plt.xlim(0, 4000)
plt.ylim(-1, 1)
plt.title('Onda Ruido')

plt.subplot(4, 1, 3)
plt.plot(w12)
plt.ylim(-2, 2)
plt.xlim(0, 3000)
plt.title('Onda Original + Ruidosa')

plt.subplot(4, 1, 4)
plt.plot(freqs[:SAMPLE//2], np.abs(fft_w12)[:SAMPLE//2])
plt.title('Frecuencias en las Ondas (FFT)')
plt.xlim(0, 1200)

plt.tight_layout()
plt.show()