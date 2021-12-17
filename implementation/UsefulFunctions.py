import numpy as np


def calculate_age_intervals(ages):
    age_frequencies = [0] * 10

    for counter in range(0, len(ages)):
        number = ages[counter]

        if 10 < number <= 15:
            age_frequencies[0] += 1
        elif 15 < number <= 20:
            age_frequencies[1] += 1
        elif 20 < number <= 25:
            age_frequencies[2] += 1
        elif 25 < number <= 30:
            age_frequencies[3] += 1
        elif 30 < number <= 40:
            age_frequencies[4] += 1
        elif 40 < number <= 50:
            age_frequencies[5] += 1
        elif 50 < number <= 60:
            age_frequencies[6] += 1
        elif 60 < number <= 70:
            age_frequencies[7] += 1
        elif 70 < number <= 80:
            age_frequencies[8] += 1
        elif number > 80:
            age_frequencies[9] += 1

    return age_frequencies


def create_laplace_noised_array(data):
    # Set parameters for Laplace function implementation
    location = 1.0
    scale = 1.0

    # Find actual data count
    # Gets random laplacian noise for all values
    laplacian_noise = np.random.laplace(location, scale, len(data))

    noise = laplacian_noise.tolist()

    noisy_data = np.array(data) + noise

    result = noisy_data.astype(int)

    return calculate_age_intervals(result.tolist())