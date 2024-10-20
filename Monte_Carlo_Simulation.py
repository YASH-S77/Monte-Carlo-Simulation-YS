import numpy as np

# Function to simulate coin toss
def coin_toss_simulation(n_tosses, n_experiments):
    results = []
    for _ in range(n_experiments):
        tosses = np.random.choice(['H', 'T'], size=n_tosses)
        heads_count = np.sum(tosses == 'H')
        results.append(heads_count)
    return results

# Function to calculate theoretical probability of exactly k heads
def theoretical_probability(n_tosses, k):
    from math import comb
    probability = comb(n_tosses, k) * (0.5 ** k) * (0.5 ** (n_tosses - k))
    return probability

# Function to calculate probability from simulation results
def calculate_probability(results, k):
    count_k_heads = results.count(k)
    probability = count_k_heads / len(results)
    return probability

# Parameters
n_experiments = 1000

# Simulate for 25, 75, and 150 tosses
tosses_list = [25, 75, 150]
results_dict = {}

for n_tosses in tosses_list:
    results = coin_toss_simulation(n_tosses, n_experiments)
    results_dict[n_tosses] = results

# Display results and calculate probabilities
for n_tosses, results in results_dict.items():
    print(f"Results for {n_tosses} tosses (first 10 outcomes):")
    print(results[:10])  # Display first 10 outcomes for brevity

    # Determine k based on the number of tosses
    if n_tosses == 25:
        k = 12  # For example, we can use 12 heads
    elif n_tosses == 75:
        k = 37  # For example, we can use 37 heads
    elif n_tosses == 150:
        k = 75  # For example, we can use 75 heads

    # Theoretical probability
    theoretical_prob = theoretical_probability(n_tosses, k)
    print(f"Theoretical probability of getting exactly {k} heads in {n_tosses} tosses: {theoretical_prob:.4f}")

    # Monte Carlo probability
    monte_carlo_prob = calculate_probability(results, k)
    print(f"Monte Carlo probability of getting exactly {k} heads in {n_tosses} tosses: {monte_carlo_prob:.4f}")
    print("\n")


