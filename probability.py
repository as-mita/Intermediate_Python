import numpy as np
import matplotlib.pyplot as plt

# One random roll
print(np.random.randint(1, 7))

# Ten rolls
few_rolls = np.random.randint(1, 7, size=10)
print(few_rolls)

# Thousand rolls
many_rolls = np.random.randint(1, 7, size=1000)
print(many_rolls)