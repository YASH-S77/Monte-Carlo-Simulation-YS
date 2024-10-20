import numpy as np

# Function to generate sequences of 1s and 2s
def generate_sequences(n_tosses, n_experiments):
    sequences = []
    for _ in range(n_experiments):
        sequence = np.random.choice([1, 2], size=n_tosses)
        sequences.append(sequence)
    return sequences

# Parameters
n_experiments = 1

# Generate sequences for 10, 50, and 100 tosses
tosses_list = [25, 75, 150]
sequences_dict = {}

for n_tosses in tosses_list:
    sequences = generate_sequences(n_tosses, n_experiments)
    sequences_dict[n_tosses] = sequences  # Fixed indentation here

# Display results
for n_tosses, sequences in sequences_dict.items():
    print(f"Results for {n_tosses} tosses:")
    for sequence in sequences:
        print(sequence)
    print("\n")

