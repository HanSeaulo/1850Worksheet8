'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''

import pandas
import matplotlib.pyplot as matplot

dateArray = list()
pollutionArray = list()

with open("leeds-centre-air-quality.csv", newline='') as file1:
    for line in file1:
        date, pm25, pm10, o3, no2 = line.split(',')
        if(date == ""):
            break
        if(date == "date"):
            continue
        dateArray.append(date)
        pollutionArray.append((int(pm25)+int(pm10)+int(o3)+int(no2))/4)
        #print(f"date:{date}, pm25:{pm25}, pm10:{pm10}, o3:{o3}, no2:{no2}")

matplot.suptitle('Hanan Jahangiri - Worksheet 8 Graph')
matplot.xlabel('Date')
matplot.ylabel('Average Pollution')

fig, ax = matplot.subplots(figsize = (12, 8))
ax.grid()
matplot.xticks(rotation = 75)
matplot.xlim(0, 30)

matplot.plot(dateArray, pollutionArray)
matplot.show()
    

