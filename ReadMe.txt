In order to create sitka5, I had to first set the values
to open the file, set reader to iterate through the assigned
file and set empty lists to append to later.

Then, in order to not hard code the location of the variables 
I needed, I created a function to automatically find 
them based on the title of the column in the csv file.
To do this I made a for loop so when I put in a specific
header row, I could call the title of that row since it switches
between data sets. This function worked for both Sitka and 
Death Valley since the TMIN, TMAX and DATE were in different
locations.

Next, I created a chart_title variable that calls the second 
row of the data set and I give it an index number to reach the 
airport name later in the code.

Next is the for loop to iterate through each row in the csv file
and pull specific data. We pulled the date, highs and lows and
then appended those specific values to the empty list created 
earlier. 

We did all of the same steps for death valley, naming the functions
'2' to differentiate them while keeping a level of familiarity.

Next we created the actual graph. To make sure we had both graphs 
in the same frame we used the subplot() function. We wanted 2
rows of the graph, one for sitka and one for death valley, then
only 1 column and we wanted sitka first so the next value was 1 and 
death valley second so we gave it the number 2. 

Then we called the chart title which is in position [1] in both of
the csv files. We plotted our lists and used some formatting functions.

Then we used the suptitle function to give the overall graph a title
and we called the chart title's once again. We formatted the date
and then used plt.show() so our graph would actually show up!
