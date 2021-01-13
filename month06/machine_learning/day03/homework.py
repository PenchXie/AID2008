import matplotlib.pyplot as plt
import math

x_list = [i * 0.1 for i in range(1, 10)]

def entropy_calculator(rate):
	entropy_value = 0
	entropy_value += rate * math.log(rate)
	entropy_value += (1 - rate) * math.log(1 - rate)

	return -entropy_value

entropy_list = [entropy_calculator(rate) for rate in x_list]
x_list.insert(0, 0)
x_list.append(1)
entropy_list.insert(0, 0)
entropy_list.append(0)

plt.plot(x_list, entropy_list, c='blue')
plt.xlabel('rate')
plt.ylabel('entropy')
plt.show()