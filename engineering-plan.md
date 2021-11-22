# Engineering plan

1. Train CNN baseline model on MNIST.
2. Use https://arxiv.org/pdf/1611.05141.pdf (or https://www.frontiersin.org/articles/10.3389/fnins.2016.00508/full) to train spiking neural network on MNIST.
3. Train CNN model using Predictive coding/Z-IL learning rule.
4. Train Spiking Neural Network using Predictive coding/Z-IL learning rule.
5. Compare the models generalization performance.

| Type/Algorithm  | Backprop | Predictive Coding |
| --------------- | -------- | ----------------- |
| Non-spiking CNN | ?        | ?                 |
| Spiking CNN     | ?        | ?                 |

7. Are predictive neural networks better at resolving ambiguity then regular bottom-up networks?

   1. Adversarial attacks?
   1. Hintons ambigious boat/house images (part-whole hierarchies).

8. Predicting next frame
   1. PredNet
