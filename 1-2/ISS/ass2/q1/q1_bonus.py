from q1_b import rand1, time
from matplotlib.pyplot import show, plot
import math

k = int(input("Enter number of coordinates: "))
pi = []
xy = rand1(time(), 2*k)
x, y = xy[:k], xy[k:]
inside = 0
for i in range(k):
    inside += int(x[i]**2 + y[i]**2 < 1)
    pi.append(math.pi - (4*inside)/(i+1))

print("Final error: ", pi[-1])
plot(pi)
show()