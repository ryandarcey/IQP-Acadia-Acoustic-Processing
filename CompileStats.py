import csv

# global vars (TODO: probably change to args)
target_csv_1 = "Test_Acoustic_123_Data.csv"
dest_csv = "stats.csv"


# calculates the total average Db level for every hour
# -> each different on the clock, not every 60 minutes/3600 seconds
def average_db_per_hour():
    with open(target_csv_1, 'r') as readfile:
        filereader = csv.reader(readfile)
        with open(dest_csv, 'w') as writefile:
            filewriter = csv.writer(writefile)

            filewriter.writerow(["Hour Number", "LAeq_dt"])   # column headers

            current_hour = -1
            hour_number = 1
            current_hour_total = 0
            current_hour_count = 0

            for row in filereader:
                if filereader.line_num % 2 == 0 or filereader.line_num <= 3:
                    # TODO: remove once there aren't extra spaces in CSVs
                    continue

                # do other stuff
                # grab info
                time = row[1].split(":")
                hour = int(time[0])
                LAeq_dt = float(row[7])

                if hour != current_hour:
                    if current_hour != -1:
                        # for second hour and on
                        filewriter.writerow([hour_number, (current_hour_total/current_hour_count)])
                        current_hour = hour
                        hour_number += 1
                        current_hour_total = 0
                        current_hour_count = 0
                    else:
                        current_hour = hour

                current_hour_total += LAeq_dt
                current_hour_count += 1


if __name__ == '__main__':
    average_db_per_hour()
