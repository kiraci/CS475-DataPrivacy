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

def create_dummy_noise(data):
    totalSize = sum(data)
    averageOfArray = totalSize / len(data)

    # If total length is lower than 100, we will just populate by 5 people
    if(len(data) <= 100):
        for i in range(len(data)):
            data[i] += 5
    # Else if total length is bigger than 100, we will add %1 percent of total size as dummy nodes to the colums which are under the average
    elif(len(data) > 100):
        for i in range(len(data)):
            if (data[i] < averageOfArray):
                data[i] += (totalSize / 100)

    return data
