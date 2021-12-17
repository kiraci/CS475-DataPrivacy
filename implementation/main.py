# import numpy
import numpy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from csv import reader
# open file in read mode

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

with open('data.csv', 'r') as read_obj:
    print('Enter interest area:')
    x = input()
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)

    count = 0
    data = []
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        if row[22] == x:

            count += 1
            data.append(int(row[19]))
    # Set parameters for Laplace function implementation
    location = 1.0
    scale = 1.0

    # Find actual data count
    # Gets random laplacian noise for all values
    Laplacian_noise = np.random.laplace(location, scale, count)

    noise = Laplacian_noise.tolist()

    noisy_data = numpy.array(data) + noise
    print(noisy_data)

    result = noisy_data.astype(int)
    x = [10, 15, 20, 25, 30,40, 50, 60, 70, 80]
    print(np.sort(result).tolist())

    result = calculate_age_intervals(result.tolist())

    # plotting
    plt.fill_between(x, result, color="skyblue", alpha=0.2)
    plt.plot(x, result, color="Slateblue", alpha=0.6)
    plt.show()

