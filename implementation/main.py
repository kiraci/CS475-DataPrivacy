# libraries
from csv import reader
import csv
from haversine import Unit
import haversine as hs
import UsefulFunctions as funcs
from charts.AreaChart import AreaChart
from charts.Histogram import Histogram
import numpy as np

# Get Input From User
print('Enter interest area:')
hobby = input()
print('Enter latitude:')
latitude = input()
print('Enter longitude:')
longitude = input()
location = (float(longitude), float(latitude))
print('Enter distance in kilometers:')
distance = input()

# open file in read mode
with open('data.csv', 'r') as read_obj:
    with open('results.csv', 'a') as write_obj:
        write_obj = csv.writer(write_obj, delimiter=',')
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)

        ages = []
        data = []
        loc = []

        for_header = True
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            if(for_header):
                write_obj.writerow(row)
                for_header = False
                continue
            # row variable is a list that represents a row in csv
            # Create K-Anonymity Age Histogram
            if row[17] == hobby:
                ages.append(int(row[18]))
                data.append(int(row[18]))
                location2 = (float(''.join(row[2].rsplit('.', 1))), float(''.join(row[1].rsplit('.', 1))))
                laplacian_noise = np.random.laplace(1.0, 1.0, 2)
                noisy_location = location2 + laplacian_noise
                difference_of_distances = hs.haversine(location, noisy_location, unit=Unit.KILOMETERS)
                if difference_of_distances < int(distance):
                    loc.append(int(row[18]))

                    # Add K-Anonymity to File
                    row[0] = row[0][0] + "**"
                    row[1] = "Longtitude - Not Provided"
                    row[2] = "Latitude - Not Provided"
                    row[8] = row[8][0] + "**"
                    row[16] = "Name - Not Provided"

                    if 10 < int(row[18]) <= 20:
                        row[18] = "10-20"
                    elif 20 < int(row[18]) <= 30:
                        row[18] = "20-30"
                    elif 30 < int(row[18]) <= 40:
                        row[18] = "30-40"
                    elif 40 < int(row[18]) <= 50:
                        row[18] = "40-50"
                    elif 50 < int(row[18]) <= 60:
                        row[18] = "50-60"
                    elif 60 < int(row[18]) <= 70:
                        row[18] = "60-70"
                    elif 70 < int(row[18]) <= 80:
                        row[18] = "70-80"
                    elif 80 < int(row[18]):
                        row[18] = "80+"

                    write_obj.writerow(row)

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

        print(funcs.create_laplace_noised_array(loc))

        # Create Area Chart For Ages with Distance - Laplace Noise
        areaChartForAgesWithLaplaceNoiseWithDistance = AreaChart([10, 20, 30, 40, 50, 60, 70, 80],
                                                                  funcs.create_laplace_noised_array(loc),
                                                                  "skyblue",
                                                                  "Slateblue")
        areaChartForAgesWithLaplaceNoiseWithDistance.run()

        print(funcs.create_dummy_noise(funcs.create_laplace_noised_array(loc)))

        # Create Area Chart For Ages with Distance - Laplace Noise and Adding Dummy Rows
        areaChartForAgesWithLaplaceNoiseWithDistanceDummy = AreaChart([10, 20, 30, 40, 50, 60, 70, 80],
                                                                  funcs.create_dummy_noise(funcs.create_laplace_noised_array(loc)),
                                                                  "skyblue",
                                                                  "Slateblue")
        areaChartForAgesWithLaplaceNoiseWithDistanceDummy.run()
