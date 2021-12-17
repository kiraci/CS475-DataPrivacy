# libraries
import numpy as np
import matplotlib.pyplot as plt
from csv import reader
import UsefulFunctions as funcs
from charts.Histogram import Histogram
from charts.AreaChart import AreaChart

# open file in read mode
with open('data.csv', 'r') as read_obj:
    print('Enter interest area:')
    x = input()
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)

    ages = []
    data = []
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        # Create K-Anonymity Age Histogram
        if row[22] == x:
            ages.append(int(row[19]))
            data.append(int(row[19]))

    # Create Histogram For Ages - K-Anonymity
    histogramForAgesWithKAnonymity = Histogram(('10-15', '16-20', '21-25', '26-30', '31-40', '41-50', '51-60', '61-70', '71-80', '80+'), funcs.calculate_age_intervals(ages), 'Ages of People with K-Anonymity', 'Age Intervals', 'Count', (0.5, 0.1, 0.5, 0.6))
    histogramForAgesWithKAnonymity.run()

    # Create Area Chart For Ages - Laplace Noise
    areaChartForAgesWithLaplaceNoise = AreaChart([10, 15, 20, 25, 30,40, 50, 60, 70, 80], funcs.create_laplace_noised_array(data), "skyblue", "Slateblue")
    areaChartForAgesWithLaplaceNoise.run()

