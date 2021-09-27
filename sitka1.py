import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=",")

#advances to the next row, but while it's doing that it saves the first row into a variable called "Header Row"
header_row = next(csv_file)

print(type(header_row))


#header row is a list, so we can use enumerate and can split that out into two parts, index value and column name
#enumerate gives you the index location and the object itself from that location

#column_header is just made up, to help make sense of it
for index, column_header in enumerate(header_row):
    print(index, column_header)

#create an empty list called highs 
highs = []

for row in csv_file:
    highs.append(int(row[5]))

print(highs)

#plt for pyplot is standard alias/best practice 
#pyplot is an object, so plt is an object as well, doing this as a chart 
import matplotlib.pyplot as plt


plt.title('Daily high temperatures, July 2018', fontsize = 16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis = "both", which = "major", labelsize = 12)

#plot allows it to create a line graph 
#this is where we imported the data into our chart, 
plt.plot(highs, c="red")

plt.show()

