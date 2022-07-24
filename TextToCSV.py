import csv

# global vars -- change as needed
read_file = "Loc2_123_Log.txt"  # .txt
dest_file = "Loc2_Acoustic_123_Data.csv"  # .csv


def txt_to_csv():
    # open .txt and .csv files
    with open(read_file) as txtfile:
        with open(dest_file, 'w', newline='') as csvfile:
            # make filewriter for csv, grab lines from txt
            filewriter = csv.writer(csvfile)
            line_list = txtfile.readlines()

            # iterate through lines to transfer them
            for line in line_list:
                l = line.strip()
                l.replace("\n", "")

                data = l.split()
                for chunk in data:
                    chunk.replace("\t", "")
                filewriter.writerow(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    txt_to_csv()
