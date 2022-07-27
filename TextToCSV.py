import csv

# global vars -- change as needed
read_file = "<name>.txt"  # .txt
dest_file = "<name>.csv"  # .csv


def txt_to_csv():
    # open .txt and .csv files
    with open(read_file) as txtfile:
        with open(dest_file, 'w', newline='') as csvfile:
            # make filewriter for csv, grab lines from txt
            filewriter = csv.writer(csvfile)
            line_list = txtfile.readlines()

            is_data = False

            # iterate through lines to transfer them
            for line in line_list:
                l = line.strip()

                data = l.split()
                for chunk in data:
                    chunk.replace("\t", "")

                if not is_data:
                    if len(data) > 0 and data[0] == "Date":
                        is_data = True
                    elif len(data) > 0 and data[0] == "#CheckSum":
                        is_data = False
                    else:
                        continue

                filewriter.writerow(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    txt_to_csv()
