import csv
import sys

n = len(sys.argv)
print("Total arguments passed:", n)
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

# global variables: (change based on input/output files wanted)
if n > 1:
    read_file = sys.argv[1]
    if n > 2:
        dest_file = sys.argv[2]
    else:
        dest_file = "Test_Acoustic_123_Data.csv"  # .csv
else:
    read_file = "_TEST_123_Log.txt"  # .txt

def txt_to_csv():
    # open .txt and .csv files
    with open(read_file) as txtfile:
        with open(dest_file, 'w') as csvfile:
            # make filewriter for csv, grab lines from txt
            filewriter = csv.writer(csvfile)
            line_list = txtfile.readlines()

            #x = 0
            # iterate through lines to transfer them
            is_next_line_data = False
            for line in line_list:
                l = line.strip()

                #if x > 500:
                    #return

                if is_next_line_data:
                    # if it's actual data
                    l.replace("\n", "")
                    data = l.split()
                    for chunk in data:
                        chunk.replace("\t", "")
                    filewriter.writerow(data)
                else:
                    # if it's info BEFORE the start of the data
                    if "#" in l and "Results" in l:
                        # don't separate data lines by ":"
                        is_next_line_data = True

                    #l.replace("\t", "")
                    l.replace("\n", "")
                    info = []
                    #if ":" in l:
                    #    info = l.split(":")
                    #else:
                    info.append(l)  # if you give writerow() a string, it puts one character per column
                    print(info)
                    filewriter.writerow(info)
                #x += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    txt_to_csv()
