import matplotlib
import numpy as np
import math
import matplotlib.pyplot as plt


def sigmoid(z):
  return 1 / (1 + np.exp(-z))

# Define hyperparameters
period = 10
num_neurons = 10
# Define the time step constant
s = complex(np.cos(np.pi / period), np.sin(np.pi / period))

# Each weight multiply adds time step s.
W = np.random.randn(num_neurons, num_neurons) * s
N = np.zeros((num_neurons, 1)) * complex(1, 0)

# Learning rate
l = 0.4
# Forget rate
gamma = 0.1

# Training steps
steps = 100
xs = np.linspace(0, 2 * np.pi, steps)
y_history = []
for i, x in enumerate(xs):
  y = 0.5 * (np.sin(x) + 1) * (s ** i)
  N[0][0] = y

  y_history.append(abs(y))

  #print("N:")
  #print(N)
  
  H = W @ N
  A = sigmoid(abs(H)) # Only look at magnitude when activating
  A = A + H.imag * 1j

  #print("A:")
  #print(A)

  # This doesn't make sense. Should be compared to last hidden state or activation? 
  P = (N @ A.T).imag
  t.append(P[1][2])

  print(P)
  
  #print("P")
  #print(P)

  U = (l * P * A.real - gamma) * W.real
  W = np.tanh(W + U)
  N = A
  #W = np.tanh(W)

  #W += l * 

  # w += (lambda * phase * A - gamma) * w

plt.plot(y_history)
plt.show()