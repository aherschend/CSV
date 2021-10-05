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

for row in reader:
    try: 
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        dates.append(the_date)
        highs.append(int(row[5]))
        lows.append(int(row[6]))

fig = plt.figure()

plt.title("SITKA AIRPORT, AK US")
plt.xlabel("", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis = "both", which = "major", labelsize = 12)

plt.plot(dates, highs, c = "red")
plt.plot(dates, lows, c = "blue")

plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1)

fig.autofmt_xdate()

plt.show()



# for Death Valley

open_file2 = open("death_valley_2018_simple.csv","r")


