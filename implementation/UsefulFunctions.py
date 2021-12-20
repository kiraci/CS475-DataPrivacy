import numpy as np


def calculate_age_intervals(ages):
    age_frequencies = [0] * 8

    for counter in range(0, len(ages)):
        number = ages[counter]

        if 10 < number <= 20:
            age_frequencies[0] += 1
        elif 20 < number <= 30:
            age_frequencies[1] += 1
        elif 30 < number <= 40:
            age_frequencies[2] += 1
        elif 40 < number <= 50:
            age_frequencies[3] += 1
        elif 50 < number <= 60:
            age_frequencies[4] += 1
        elif 60 < number <= 70:
            age_frequencies[5] += 1
        elif 70 < number <= 80:
            age_frequencies[6] += 1
        elif 80 < number:
            age_frequencies[7] += 1

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


def normalize_array(arr):
    max_number = max(arr)
    min_number = min(arr)
    average = sum(arr) / len(arr) / 2

    length_of_array = len(arr)
    formula = 0

    for i in range(0, length_of_array):
        if (length_of_array < 50):
            formula = 3
        elif(length_of_array < 1000):
            formula = (max_number - min_number) % 20
        elif(length_of_array > 10000):
            formula = 200

        if(arr[i] < average):
            arr[i] += formula
    return arr
