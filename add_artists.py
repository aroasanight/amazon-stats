# import listening.csv
import csv

# open the csv file
with open('listening.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# also import artists.csv
with open('artists.csv', 'r') as f:
    reader = csv.reader(f)
    artists = list(reader)

# for all items except the first, [10] is the artist id.
# for all such items, append to the end the matching artist name from artists.csv
for i in range(1, len(data)):
    for artist in artists:
        if data[i][10] == artist[0]:
            data[i].append(artist[1])
            break

# save the new data to a new csv file
# listening_artist.csv
with open('listening_artist.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)