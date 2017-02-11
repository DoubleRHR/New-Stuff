import matplotlib.pyplot as plt


def intan(n):
    return 180 -(360/n)

n_values = range(4, 500)
plt.plot(n_values, list(map(intan, n_values)))
plt.show()
