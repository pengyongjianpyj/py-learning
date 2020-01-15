import matplotlib.pyplot as plt

squares = [0]
for i in range(1, 20):
    squares.append(2**i)
plt.plot(squares)
plt.show()