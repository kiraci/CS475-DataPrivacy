from csv import reader
# open file in read mode
with open('data.csv', 'r') as read_obj:
    print('Enter interest area:')
    x = input()
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    long = 0
    la = 0
    count = 0
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        if row[22] == x:
            long += float(row[1])
            la += float(row[2])
            count += 1

    print(long/count, la/count)