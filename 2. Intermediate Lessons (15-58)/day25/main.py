# with open("weather_data.csv") as weather_file:
#     weather_data = weather_file.readlines()
#     for row in weather_data:
#         transformed_row = row.strip()
#         print(transformed_row)

import csv

with open("day25/weather_data.csv") as weather_file:
    data = csv.reader(weather_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)


import pandas

pandas.read_csv("day25/weather_data.csv")
print(data["temp"])