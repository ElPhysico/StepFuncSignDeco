import json
import pandas as pd
import numpy as np
import math
from scipy.fft import fft, fftshift, fftfreq, ifft, rfft, irfft
from scipy.signal import blackman
import matplotlib.pyplot as plt

# from scipy.fft import fft, fftfreq
# # Number of sample points
# N = 600
# # sample spacing
# T = 1.0 / 800.0
# x = np.linspace(0.0, N*T, N, endpoint=False)
# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
# yf = fft(y)
# xf = fftfreq(N, T)[:N//2]
# print(xf)
# import matplotlib.pyplot as plt
# plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
# plt.grid()
# plt.show()

with open ("config.json", "r") as config_file:
    config = json.load(config_file)

layers = config['layers']
N = config['numAtoms']
T = config['distanceAtoms']
length = (N - 1) * T
N *= 5


df = pd.read_csv(config['file_in'], sep = '\t')
df = df.rename(columns={"#radGap": "radGap"})

w = blackman(N)

for id in range(20):
    offset = df.loc[id]['offset']
    gap = df.loc[id]['radGap']

    y = np.array([])
    for k in range(N):
        count = 0
        pos = 5 * (length) + k * T
        for layer in range(layers):
            if (math.fmod(pos - layer * offset, length + gap) <= length):
                count += 1
        y = np.append(y, count / layers)

    yf = rfft(y)
    ywf = rfft(y * w)
    ywplot = ywf
    # ywplot = fftshift(ywplot)
    yplot = yf
    # yplot = fftshift(yplot)
    yif = irfft(yf)

    # x = np.linspace(0.0, N * T, N, endpoint=False)
    # xf = fftfreq(N, T)
    # print(xf)
    # xplot = xf
    # xplot = fftshift(xplot)

    testy = np.copy(yf)
    help = 1 / N * np.abs(testy)

    sum = 0
    weightsum = 0
    for key, value in enumerate(help):
        if key == 0:
            continue
        sum += key * value
        weightsum += value

    print("average frequency: " + str(sum / weightsum))
    print("average wavelength: " + str(weightsum / sum))

    for key, value in enumerate(help):
        # if value > 0.1:
        #     print(key, value)
        #     testy[key] = 0 + 0j
        if value < 0.001:
            print(key, value)
            testy[key] = 0 + 0j


    maxindex = np.argmax(testy)
    print(maxindex)
    yif2 = irfft(testy)


    f, (ax0, ax1, ax2) = plt.subplots(3, 1, sharex=False)
    ax0.plot(y)
    # ax1.plot(1 / (N * layers) * np.abs(yplot), '-b')
    ax1.plot(1 / N * np.abs(yplot))
    ax1.plot(1 / N * np.abs(testy))
    ax2.plot(np.abs(yif))
    ax2.plot(np.abs(yif2))
    ax0.grid()
    ax1.grid()
    ax2.grid()
    ax0.set_ylim([-0.1,1.1])
    ax1.set_ylim([0,0.01])
    ax2.set_ylim([-0.1,1.1])
    ax0.set_title('Signal', color='red')
    ax1.set_title('FFT', color='red')
    ax2.set_title('Inverse FFT', color='red')
    plt.suptitle('Sample ' + str(id) + ' -- check value: ' + str(df.loc[id]['check']))
    f.set_size_inches(8, 10)
    plt.show()











# from scipy.signal import blackman
# w = blackman(N)
# ywf = rfft(y * w)

# import matplotlib.pyplot as plt
# axes = plt.gca()
# axes.set_xlim([xmin,xmax])
# axes.set_ylim([0,100])
# plt.plot(xf, np.abs(yf))
# plt.plot(np.abs(yf))



x = np.zeros(500)
x += 2
x[50:100] = 1
x[150:200] = 1
x[250:300] = 1
x[350:400] = 1
x[450:500] = 1


X = rfft(x)
# X = fftshift(X)

f, (ax0, ax1) = plt.subplots(2, 1, sharex=False)

ax0.plot(x)
ax0.set_ylim(-0.1, 2.1)

ax1.plot(np.abs(X))
# ax1.set_ylim(-5, 55)

# plt.plot(np.abs(X))
#
plt.show()

# def gen_sine_wave(freq, sample_rate, duration):
#     x = np.linspace(0, duration, sample_rate * duration, endpoint = False)
#     frequencies = x * freq
#     y = np.sin((2 * np.pi) * frequencies)
#     return x, y
#
#
# sample_rate = 44100
# duration = 5
# x, y = gen_sine_wave(4000, sample_rate, duration)
#
# N = sample_rate * duration
# yf = rfft(y)
# print(y)
# print(yf)
# xf = rfftfreq(N, 1 / sample_rate)
# # plt.plot(xf, np.abs(yf))
# plt.plot(x, y)
# plt.grid()
# plt.show()
