import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 105)
ax.set_ylim(-2, 2)
line, = ax.plot(0, 0)

def animation_frame(i):
	x_data.append(i)
	y_data.append(math.sin(i))

	line.set_xdata(x_data)
	line.set_ydata(y_data)
	return line

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 100, 0.1), interval=20)
plt.show()
animation.save('anim2.gif',fps=50)
