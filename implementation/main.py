# libraries
import numpy as np
import matplotlib.pyplot as plt
from csv import reader
import sys

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

# open file in read mode
with open('data.csv', 'r') as read_obj:
    print('Enter interest area:')
    x = input()
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)

    ages = []

    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        # Create K-Anonymity Age Histogram
        if row[22] == x:
            ages.append(int(row[19]))

    # create dataset
    height = calculate_age_intervals(ages)
    bars = ('10-15', '16-20', '21-25', '26-30', '31-40', '41-50', '51-60', '61-70', '71-80', '80+')
    x_pos = np.arange(len(bars))

    # Create bars and choose color
    plt.bar(x_pos, height, color=(0.5, 0.1, 0.5, 0.6))

    # Add title and axis names
    plt.title('Ages of People with K-Anonymity')
    plt.xlabel('Age Intervals')
    plt.ylabel('Count')

    # Create names on the x axis
    plt.xticks(x_pos, bars)

    # Show graph
    plt.show()
