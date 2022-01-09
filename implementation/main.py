# libraries
from csv import reader
from haversine import Unit
import haversine as hs
import UsefulFunctions as funcs
from charts.AreaChart import AreaChart
from charts.Histogram import Histogram
import numpy as np


print('Enter interest area:')
hobby = input()
print('Enter latitude:')
latitude = input()
print('Enter longitude:')
longitude = input()
location = (float(latitude), float(longitude))
Bprint('Enter distance in meters:')
distance = input()

# open file in read mode
with open('data.csv', 'r') as read_obj:

    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)

    ages = []
    data = []
    loc = []

    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        # Create K-Anonymity Age Histogram
        if row[21] == hobby:

            location2 = (float(row[2]), float(row[1]))
            laplacian_noise = np.random.laplace(1.0, 1.0, 2)
            noisy_location = location2 + laplacian_noise
            if hs.haversine(location, noisy_location, unit=Unit.METERS) < int(distance):
                ages.append(int(row[22]))
                data.append(int(row[22]))
                loc.append(int(row[22]))



    # Create Histogram For Ages - K-Anonymity
    histogramForAgesWithKAnonymity = Histogram(('10-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '80+'),
                                               funcs.calculate_age_intervals(ages),
                                               'Ages of People with K-Anonymity',
                                               'Age Intervals',
                                               'Count',
                                               (0.5, 0.1, 0.5, 0.6))
    histogramForAgesWithKAnonymity.run()

    # Create Area Chart For Ages - Laplace Noise
    areaChartForAgesWithLaplaceNoise = AreaChart([10, 20, 30, 40, 50, 60, 70, 80],
                                                 funcs.create_laplace_noised_array(data),
                                                 "skyblue",
                                                 "Slateblue")
    areaChartForAgesWithLaplaceNoise.run()

    print(loc)
    print(funcs.create_laplace_noised_array(loc))

    # Create Area Chart For Ages with Distance - Laplace Noise
    # areaChartForAgesWithLaplaceNoiseWithDistance = AreaChart([10, 20, 30, 40, 50, 60, 70, 80],
    #                                                          funcs.create_laplace_noised_array(loc),
    #                                                          "skyblue",
    #                                                          "Slateblue")
    # areaChartForAgesWithLaplaceNoiseWithDistance.run()
    #
    # areaChartForAgesWithLaplaceNoiseWithDistancea = AreaChart([10, 20, 30, 40, 50, 60, 70, 80],
    #                                              funcs.normalize_array(funcs.create_laplace_noised_array(loc)), "skyblue", "Slateblue")
    # areaChartForAgesWithLaplaceNoiseWithDistancea.run()

