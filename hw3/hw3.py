import math
import numpy
import matplotlib.pyplot as plt

t0 = 0
tfinal = 5
dt = 0.1

timesteps = int((tfinal - t0) / dt)

x = numpy.zeros(timesteps)
y = numpy.zeros(timesteps)
t = numpy.zeros(timesteps)

x[0] = float(input("Enter a value for x0: ")) 
y[0] = float(input("Enter a value for y0: "))
print()

a = float(input("Enter a lethality coefficient for x (alpha): "))
b = float(input("Enter a lethality coefficient for y (beta): "))
print()

xRe = int(input("Enter the number of reinforcement events for x: "))
yRe = int(input("Enter the number of reinforcement events for y: "))
print()

# truncate the lists so that they contain no more than 3 items each
xevents = min(max(0, xRe), 3)
yevents = min(max(0, yRe), 3)

xp = float(input("Enter level at which a reinforcement occurs for x as a percentage of (x0) initial force level: "))
yp = float(input("Enter level at which a reinforcement occurs for y as a percentage of (y0) initial force level: "))
print()

# truncate input to ensure it fits within the range (10% - 80%)
xp = min(max(10, xp), 80) 
yp = min(max(10, yp), 80)
print()

xrsize = float(input("Enter reinforcement size for x as a percentage of (x0) initial force level: "))
yrsize = float(input("Enter reinforcement size for y as a percentage of (y0) initial force level: "))
print()

# truncate input to ensure it sitf within the range (10% - 50%)
xrsize = min(max(10, xp), 50)
yrsize = min(max(10, yp), 50)
print()

xrsize = math.ceil((xrsize/100) * x[0])
yrsize = math.ceil((yrsize/100) * y[0])

a1 = float(input("Enter a lethality coefficient for x reinforcments (alpha1): "))
b1 = float(input("Enter a lethality coefficient for y reinforcements (beta1): "))

for i in range(timesteps -1):
    x[i+1] = max(0, x[i] - dt * (y[i] * b))
    y[i+1] = max(0, y[i] - dt * (x[i] * a))
    t[i+1] = t[i] + dt
    
    if(x[i+1] <= (xp/100) * x[0] and xevents > 0):
      x[i+1] += xrsize
      a = a1
      xevents -= 1

    if(y[i+1] <= (yp/100) * y[0] and yevents > 0):
      y[i+1] += yrsize
      b = b1
      yevents -= 1

plt.plot(t, x, label = "x")
plt.plot(t, y, label = "y")

plt.xlabel("Time")
plt.ylabel("Survivors")
plt.title("Lanchester's Law for aimed fire")
plt.legend()
plt.show()
