# Notes

## Brain score

http://www.brain-score.org/#about

https://www.frontiersin.org/articles/10.3389/fncom.2010.00019/full

https://en.wikipedia.org/wiki/Free_energy_principle

https://www.youtube.com/watch?v=b1hEc6vay_k

### An Approximation of the Error Backpropagation Algorithm in a Predictive Coding Network with Local Hebbian Synaptic Plasticity

https://direct.mit.edu/neco/article/29/5/1229/8261/An-Approximation-of-the-Error-Backpropagation

### Predictive coding, active inference and the jazz!

https://medium.com/@solopchuk

### Predictive coding network

https://openreview.net/pdf?id=Hy8hkYeRb

### Research questions

- What are the constraints of biologically learning?
- According to the current litterature what are the biological constraints of biological learning?

- What is predictive coding and how can it approximate backpropagation under biological constraints?
- Can predictive coding approximate backpropagation and if so, how well does it perform under biological plausible constraints?

- How can active inference and the free energy principle be used in reinforcement learning
- What is the correspondance between active inference and the free energy principle and current reinforcement methods?

The derivative problem problematizes the need for the derivative of the activation function (ex. sigmoid or ReLU used in the forward pass) in order to back-propagate the error signal to the early layers of the network.
The spiking problem as biological neurons communicate using sparse binary spikes as opposed to the dense real-valued signals used in artificial neural networks.
The timing problem which also relates to the spiking problem, since biological neurons operate in time and might encode information in the temporality of the spikes. Artificial neural networks tend to ignore this.

## Derivation of rate

$$
  V(t) = (V(0) - j)e^{-t/t_{RC}} + j \\
  1 = - je^{-t/t_{RC}} + j \\
  1 - j = - je^{-t/t_{RC}} \\
  \frac{1 - j}{j} = - e^{-t/t_{RC}} \\
  \frac{1}{j} - 1 = - e^{-t/t_{RC}} \\
  1 -\frac{1}{j} = e^{-t/t_{RC}} \\
  \log(1 -\frac{1}{j}) = \frac{-t}{t_{RC}} \\
  t = -t_{RC}\log(1 -\frac{1}{j}) \\
  r = \frac{1}{-t_{RC}\log(1 -\frac{1}{j})} \\
$$

Interesting about spiking neural networks and feature binding.
https://www.youtube.com/watch?v=aisgNLypUKs

Fusing batch normalization and convolution in runtime
https://nenadmarkus.com/p/fusing-batchnorm-and-conv/

Predictive Coding Models of Perception
https://www.youtube.com/watch?v=P0yVuoATjzs
