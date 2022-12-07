import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('house_price.txt', delimiter=',')
X = data[:, 0]
y = data[:, 1]
coef = np.polyfit(X,y,1)
poly1d_fn = np.poly1d(coef)
plt.xlabel('size')
plt.ylabel('price')
plt.title('House Dataset')
plt.plot(X,y, 'yo', X, poly1d_fn(X), 'k')
plt.figure()
plt.show()
