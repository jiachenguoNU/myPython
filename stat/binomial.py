import matplotlib.pyplot as plt
from scipy.stats import binom
import numpy as np

# --- 1. Define the parameters for the binomial distribution ---
n = 100  # Number of trials
p = 0.2 # Probability of success on a single trial

# --- 2. Generate the possible outcomes ---
# The number of successes (k) can range from 0 to n.
k_values = np.arange(0, n + 1)

# --- 3. Calculate the probability for each outcome ---
# The binom.pmf function calculates the Probability Mass Function (PMF),
# which gives the probability of getting exactly 'k' successes.
probabilities = binom.pmf(k_values, n, p)

# --- 4. Plot the distribution ---
plt.figure(figsize=(12, 6)) # Set the figure size for better readability
plt.bar(k_values, probabilities, color='skyblue', edgecolor='black')

# --- 5. Add labels and a title for clarity ---
plt.title(f'Binomial Distribution (n={n}, p={p})', fontsize=16)
plt.xlabel('Number of Successes (k)', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.xticks(k_values) # Ensure all integer values of k are shown on the x-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()