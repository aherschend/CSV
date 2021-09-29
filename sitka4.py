import csv
import matplotlib as plt
from datetime import datetime 



open_file = open("death_valley_2018_simple.csv", "r")

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
lows = []
dates = []

for row in csv_file:
    try:
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {the_date}")
        # what does the f do? new method introduced, allows us to incorporate variables directly into our statements, called the f string method
    else:
        lows.append(int(row[5]))
        dates.append(the_date)
        highs.append(int(row[4]))

#print(highs)
#print(lows)
#print(dates)

'''
#plt for pyplot is standard alias/best practice 
#pyplot is an object, so plt is an object as well, doing this as a chart 
import matplotlib.pyplot as plt

fig = plt.figure()

plt.title('Daily high and low temperatures, 2018', fontsize = 16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis = "both", which = "major", labelsize = 12)

#plot allows it to create a line graph 
#this is where we imported the data into our chart, 
#dates on x axis and highs on y

plt.plot(dates, highs, c="red")
plt.plot(dates,lows, c='blue')

plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)


fig.autofmt_xdate()

plt.show()

#subplot (row, column, index)
        #(1,2,4)

plt.subplot(2,1,1)
plt.plot(dates, highs, c="red")
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows,c="blue")
plt.title("Lows")

#supertitle is for the whole entire sheet not just the individual graphs

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()


'''