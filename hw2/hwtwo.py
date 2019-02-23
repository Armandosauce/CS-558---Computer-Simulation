import numpy
import matplotlib.pyplot as plt

t0 = 0
tfinal = 3
dt = 0.1

timesteps = int((tfinal - t0) / dt)

x = numpy.zeros(timesteps)
y = numpy.zeros(timesteps)
t = numpy.zeros(timesteps)

x[0] = float(input("Enter a value for x0: ")) 
y[0] = float(input("Enter a value for y0: "))

a = float(input("Enter a lethality coefficient for x (alpha): "))
b = float(input("Enter a lethality coefficient for y (beta): "))

for i in range(timesteps -1):
    x[i+1] = max(0, x[i] - dt * (y[i] * b))
    y[i+1] = max(0, y[i] - dt * (x[i] * a))
    t[i+1] = t[i] + dt

plt.plot(t, x, label = "x")
plt.plot(t, y, label = "y")

plt.xlabel("Time")
plt.ylabel("Survivors")
plt.title("Lanchester's Law for aimed fire")
plt.legend()
plt.show()
