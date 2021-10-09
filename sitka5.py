import csv
import matplotlib as plt
from matplotlib import pyplot as plt
from datetime import datetime


# for Sitka
open_file = open("sitka_weather_2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter = ",")
reader = csv.reader(open_file)
header_row = next(reader)

dates = []
highs = []
lows = []

def index(title,key):
    for index in title:
        if index == key:
            return title.index(index)

chart_title = next(csv_file)

# need to define date_index here that way it's not hard-coded
for row in reader:
    try: 
        the_date = datetime.strptime(row[index(header_row, "DATE")], '%Y-%m-%d')
        high = int(row[int(index(header_row, "TMAX"))])
        low = int(row[int(index(header_row, "TMIN"))])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        dates.append(the_date)
        highs.append(int(row[int(index(header_row, "TMAX"))]))
        lows.append(int(row[int(index(header_row, "TMIN"))]))



# for Death Valley

open_file2 = open("death_valley_2018_simple.csv","r")
csv_file2 = csv.reader(open_file2, delimiter = ",")
reader2 = csv.reader(open_file2)
header_row2 = next(reader2)

dates2 = []
highs2 = []
lows2 =[]

chart_title2 = next(csv_file2)

for row in reader2:
    try:
        the_date2 = datetime.strptime(row[index(header_row2, "DATE")], '%Y-%m-%d')
        high2 = int(row[int(index(header_row2, "TMAX"))])
        low2 = int(row[int(index(header_row2, "TMIN"))])
    except ValueError:
        print(f"Missing data for {the_date2}")
    else:
        dates2.append(the_date2)
        highs2.append(int(row[int(index(header_row2, "TMAX"))]))
        lows2.append(int(row[int(index(header_row2, "TMIN"))]))


fig = plt.figure()

# for sitka
plt.subplot(2,1,1)
plt.title(chart_title[1])
plt.plot(dates, highs, c = "red")
plt.plot(dates, lows, c = "blue")
plt.xlabel("", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis = "both", which = "major", labelsize = 12)
plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1)


# for death valley
plt.subplot(2,1,2)
plt.title(chart_title2[1])
plt.plot(dates2, highs2, c = "red")
plt.plot(dates2, lows2, c = "blue")
plt.xlabel("", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis = "both", which = "major", labelsize = 12)
plt.fill_between(dates2, highs2, lows2, facecolor = "blue", alpha = 0.1)


plt.suptitle(f"Temperature Comparison between {chart_title[1]} and {chart_title2[1]}") 



fig.autofmt_xdate()

plt.show()




#plt.subplot(rows, columns, order of plot)

