#!/usr/bin/env python

import matplotlib.pyplot as plt
import math

xarr = []
yarr = []

for i in range(1, 20):
    x = ((2 / math.sqrt(3)) * i) * math.cos((math.pi / 6) * i)
    xarr.append(x)
    y = ((2 / math.sqrt(3)) * i) * math.sin((math.pi / 6) * i)
    yarr.append(y)

# For cross
# plt.plot(xarr, yarr, "x", label='Aₙ')

# For lines
# plt.plot(xarr, yarr, label='Aₙ')

# For lines and cross
plt.plot(xarr, yarr, label='Aₙ', marker='x')

plt.xlabel('u→')
plt.ylabel('v→')
plt.title("Zₙ₊₁ = (1 + i × (√3/3)³) × zₙ")
plt.legend()

plt.show()
