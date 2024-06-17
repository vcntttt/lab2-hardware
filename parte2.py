import numpy as np
import matplotlib.pyplot as plt

FREQ_0 = 9000; FREQ_1 = 5000; FREQ_2 = 100
SAMPLE = 20000; S_RATE = 20000.0
nMAX = 20000

aW = [
    [2*np.sin(2*np.pi * FREQ_0 * i/S_RATE) for i in range(SAMPLE)],
    [2*np.sin(2*np.pi * FREQ_1 * i/S_RATE) for i in range(SAMPLE)],
    [2*np.sin(2*np.pi * FREQ_2 * i/S_RATE) for i in range(SAMPLE)]
]

aS = [
    np.array(aW[0]) + np.array(aW[1]),
    np.array(aW[0]) + np.array(aW[2]),
    np.array(aW[1]) * np.array(aW[2])
]

def Filter_Comp(aV, nA):
    aF = np.zeros(len(aV))
    aF[0] = aV[0]
    for i in range(1, nMAX):
        aF[i] = nA * aV[i] + (1.0 - nA) * aF[i - 1]
    return aF

aF1 = Filter_Comp(aS[0], 0.3)
aF2 = Filter_Comp(aS[1], 0.2)
aF3 = Filter_Comp(aS[2], 0.1)

plt.figure(figsize=(8, 10))

plt.subplot(3, 1, 1)
plt.plot(aS[0], color='blue')
plt.plot(aF1, color='red')
plt.title("Signal 1")
plt.ylim(-6, 6)
plt.xlim(0, 200)

plt.subplot(3, 1, 2)
plt.plot(aS[1], color='blue')
plt.plot(aF2, color='red')
plt.title("Signal 2")
plt.ylim(-15, 15)
plt.xlim(0, 200)

plt.subplot(3, 1, 3)
plt.plot(aS[2], color='blue')
plt.plot(aF3, color='red')
plt.title("Signal 3")
plt.ylim(-30, 30)
plt.xlim(0, 200)

plt.tight_layout()
plt.show()