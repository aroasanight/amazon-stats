# import csvs
import csv

filenames = ['2020-2','2021-1','2021-2','2022-1','2022-2']

# load artists.csv into artists
with open('artists.csv', 'r') as f:
    reader = csv.reader(f)
    artists = list(reader)

for filename in filenames:
    with open(filename+".csv", 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    # "['Carry On', 'B08HK566PS', '333000', 'trackFinished', '333000', 'B0038ZLSDC']",206

    new_csv = []
    for data_selected in data:

        data_current = str(data_selected[0]).replace('''""''',"'").replace('["',"['").replace('",',"',")
        print(data_current)
        data_current = data_current.replace("['","").replace("']","").split("', '")
        data_current.append(data_selected[1])

        if int(data_current[6]) < 7:
            pass
        elif data_current[0] == "Not Available":
            pass
        else:

            data_current.pop(1)
            artist_id = data_current.pop(4)

            for artist_data in artists:
                if artist_id == artist_data[0]:
                    data_current.insert(1,artist_data[1])
                    break

            data_current[0] = data_current[0].replace(" [Explicit]","")

            data_current.pop(2)
            data_current.pop(2)
            data_current.pop(2)

            # print(data_current)
            new_csv.append(data_current)

    # keep only first 250 rows
    new_csv = new_csv[:250]

    print(new_csv)

    # save new_csv to 2020-2-artist.csv
    with open(filename+"_new.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(new_csv)