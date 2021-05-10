import matplotlib.pyplot as plt
import numpy as np
import math

# Global variables
samples = 100
k = 200
L = 10
# L = 2 * math.pi


# Functions
def g(i, k, t):
    if (L / k * (i - 1) <= t and t < L / k * i):
        return math.sqrt(k / samples)
    else:
        return 0

def f(t):
    return t

def h(t):
    return (t - math.pi) ** 2 - 5

def signal(t):
    a = L / 5
    b = a / 2
    if (math.fmod(t, a) <= b):
        return 1
    else:
        return 0


######################################


x = np.linspace(0, L, samples, endpoint=False)
x2 = np.linspace(0, L, 1000, endpoint=False)
x3 = np.linspace(-L, 3 * L, 5000, endpoint=False)

ys = []
for i in range(1, k + 1):
    yh = []
    for t in x3:
        yh.append(g(i, k, t))
    ys.append(yh)

# coefficients
a = []
for i in range(1, k + 1):
    c = 0
    for t in x:
        c += g(i, k, t) * h(t)
    a.append(c)

b = []
binsize = L / k
for t in x:
    b.append(a[int(t / binsize)])

y = []
yt = []
ytdraw = []

for t in x:
    help = 0
    for i in range(1, k + 1):
        help += a[i - 1] * g(i, k, t)
    yt.append(help)

for t in x2:
    y.append(h(t))
    pos = min(int(len(x) * t / x2[len(x2) - 1]), len(x) - 1)
    ytdraw.append(yt[pos])


# print(len(x))
# for key, val in enumerate(x):
#     print(key, val)


# for i in range(len(y)):
#     print(y[i], yt[i], y[i] / yt[i], 2 * math.pi)

# fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2, sharex = False)
fig, (ax0, ax1, ax2) = plt.subplots(3, 1, sharex = False)

# for i in range(k):
#     ax0.plot(x, ys[i])
ax0.plot(x2, y)
ax0.set_title('Function', color = 'blue')
ax0.set(xlabel = 'x [nm]', ylabel = 'density [counts]')

ax1.stem(a, markerfmt='.')
ax1.set_title('Weights', color = 'blue')
ax1.set(xlabel = 'Mode #', ylabel = 'weight [arb. unit]')

ax2.plot(x2, ytdraw)
ax2.set_title('Transformed function', color = 'blue')
ax2.set(xlabel = 'x [nm]', ylabel = 'density [counts]')

# for i in range(k):
#      ax3.plot(x3, ys[i])
# ax3.set_xlim([-5, 20])
# ax3.set_title('Base functions')
# ax3.set(xlabel = 'x [nm]', ylabel = 'weight [arb. unit]')

plt.subplots_adjust(hspace = 0.4)
plt.suptitle('Testing around')
fig.set_size_inches(8, 12)
plt.show()
