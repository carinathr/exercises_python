import matplotlib.pyplot as plt

r = 0.5
a = 1
n = 10

s_n = [] 

cumulative_sum = 0

for k in range(0, n):
    cumulative_sum += a*r**(k)
    s_n.append(cumulative_sum)
print(s_n)
import matplotlib.pyplot as plt
plt.plot(s_n)
