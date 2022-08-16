# importing the required module
from turtle import title
import matplotlib.pyplot as plt
from random import randrange

import numpy as np

t = np.arange(0, 10, 0.01)

# Sin plot
ax1 = plt.subplot(211)
ax1.plot(t, np.sin(2*np.pi*t), label="Yes", linestyle='dashed')


# Pre calculated plot
x = [1,2,3,4,5,6,7]
y = [2,4,1,15,19,24,-5]
  
plt.plot(x, y, label="Test Line", color='green', linestyle='dashed', marker='o',
     markerfacecolor='blue')
  
# Reverse plot
x = [1,2,3,4,5,6,7]
y = [2,4,1,15,19,24,-5][::-1]

plt.plot(x, y, label="Reverse Test Line", color='red', linestyle='dashed', marker='o',
     markerfacecolor='green')

# Random plot
ranX = []
ranY = []
for ind in range(20):
     ranX.append(ind)
     ran = randrange(100)
     ranY.append(ran)

     print("Appending " + str(ind) + ", " + str(ran))



plt.plot(ranX, ranY, label="Random Data", color='black', linestyle='dashed')

plt.xlabel('x - axis')
plt.ylabel('y - axis')
  
plt.title('Test Graph')
plt.legend()
  
plt.show()

# t = np.arange(0, 10, 0.01)

# ax1 = plt.subplot(211)
# ax1.plot(t, np.sin(2*np.pi*t))

# ax2 = plt.subplot(212, sharex=ax1)
# ax2.plot(t, np.sin(4*np.pi*t))

# plt.show()