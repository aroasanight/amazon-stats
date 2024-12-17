# import libraries
import csv
from datetime import datetime

# open the csv file
with open('listening.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    data.pop(0)

# convert the first item of each sublist to a datetime object
for i in range(len(data)):
    data[i][0] = datetime.strptime(data[i][0], "%Y-%m-%d %H:%M:%S %Z")

# find latest and earliest date from data[i][0]
latest_date = max([data[i][0] for i in range(len(data))])
earliest_date = min([data[i][0] for i in range(len(data))])

# from the earliest date, go back in time to find the closest jan 1st or july 1st
if earliest_date.month < 7:
    start_date = datetime(earliest_date.year, 1, 1)
else:
    start_date = datetime(earliest_date.year, 7, 1)

# same for the latest date, still going back
if latest_date.month < 7:
    end_date = datetime(latest_date.year, 1, 1)
else:
    end_date = datetime(latest_date.year, 7, 1)

# create list of all jan 1st and july 1st between start_date and end_date (inclusive on both ends)
date_list = []
while start_date <= end_date:
    date_list.append(start_date)
    if start_date.month == 1:
        start_date = datetime(start_date.year, 7, 1)
    else:
        start_date = datetime(start_date.year + 1, 1, 1)

# repeat once for each date
for date in date_list:
    # create new start and end date variables - with the start being `date` and the end being 6 months later
    start_date = date
    if date.month == 1:
        # 30th of june
        end_date = date.replace(month=6, day=30)
    else:
        # 31st of december
        end_date = date.replace(month=12, day=31)
    # subtract one day from the end date to make it inclusive
    end_date = end_date.replace(day=end_date.day - 1)

    # for each item in the data list, add [data[i][1], data[i][10]] to a new list if the date is between start_date and end_date, and data[i][3] is greater than 20000
    new_list = []
    for i in range(len(data)):
        if start_date <= data[i][0] <= end_date:
            if int(data[i][3]) > 20000:
                new_list.append([data[i][1], data[i][2], data[i][3], data[i][4], data[i][9], data[i][10]])
    
    # create a new list - and for each item in the new list, create a list with [text, count]
    new_list2 = []
    for i in range(len(new_list)):
        if new_list[i] not in [x[0] for x in new_list2]:
            new_list2.append([new_list[i], 1])
        else:
            for j in range(len(new_list2)):
                if new_list2[j][0] == new_list[i]:
                    new_list2[j][1] += 1
    
    # sort the list by count
    new_list2.sort(key=lambda x: x[1], reverse=True)

    # save the list to a file in csv form with the filename "yyyy-1" or "yyyy-2" where yyyy is the year of the start_date
    if start_date.month == 1:
        with open(f"{start_date.year}-1.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(new_list2)
    else:
        with open(f"{start_date.year}-2.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(new_list2)

