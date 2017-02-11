import matplotlib.pyplot as plt
import pandas as pd

x = pd.Series(range(4, 100))
y = 180 - 360 / x

plt.plot(x, y)
plt.show()
