fs = open("clam_data.txt")
time_list = []
for line in fs:
    temp = line.rstrip().split(",")
    for val in temp:
        try:
            value_int = int(val)
            if value_int > 1413229040 and value_int < 1500000000:
                time_list.append(value_int)
        except ValueError:
            continue

bins = []

