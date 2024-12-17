import csv
from datetime import datetime

data = []
counter = 0
with open('listening.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        try: 
            data.append([row[10],datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S %Z")])
        except:
            counter += 1
    if counter > 1: print("ERROR")

# reverse list order
data = data[::-1]

from selenium import webdriver
import time

# set newlist to artists.csv
try:
    with open('artists.csv', 'r') as f:
        reader = csv.reader(f)
        newlist = list(reader)
except:
    newlist = []

try:
    driver = webdriver.Chrome()
    counter3 = 0
    counter4 = 0
    for i in range(len(data)):
        if counter3 > 100:
            # save to file
            with open('artists'+str(counter4)+'.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(newlist)
            counter3 = 0
            counter4 += 1
        # check if data[i] is in newlist[i][0]
        if data[i][0] in [newlist[j][0] for j in range(len(newlist))]:
            print("skipping " + data[i][0])
        else:
            counter3 += 1
            print("looking up " + data[i][0] + " (listened on " + data[i][1].strftime("%Y-%m-%d") + ")")
            driver.get(str('https://music.amazon.co.uk/artists/' + data[i][0]))
            # wait until driver.title contains "on Amazon Music Unlimited"
            counter2 = 0
            while ("on Amazon Music Unlimited" not in driver.title) and (counter2 < 1500):
                time.sleep(0.01)
                counter2 += 1
            name = driver.title.replace(" on Amazon Music Unlimited", "")
            newlist.append([data[i][0], name])
            print("found " + data[i][0] + " as " + name)
    driver.quit()
except:
    driver.quit()

with open('artists.csv', 'w', newline='') as f:
    # write to csv
    writer = csv.writer(f)
    writer.writerows(newlist)
