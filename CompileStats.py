import csv
#import array as arr

# global vars
target_csv_1 = "Loc1_Acoustic_123_Data.csv"
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


# gets a few different stats (average LAeq per each of 24 hours,
# median LAF_min, median LAF_max)
def db_per_hour_all_days_stats():
    with open(target_csv_1, 'r') as readfile:
        filereader = csv.reader(readfile)
        with open(dest_csv, 'w') as writefile:
            filewriter = csv.writer(writefile)

            filewriter.writerow(["Hour (0-23)", "LAeq_dt", "LAFmin", "LAFmax"])  # column headers

            LAFmax_dict = {}
            LAFmin_dict = {}
            LAeq_dict = {}
            current_hour = -1
            current_LAFmax_list = []
            current_LAFmin_list = []
            current_LAeq_list = []

            for i in range(0, 24):
                LAFmax_dict[i] = []
                LAFmin_dict[i] = []
                LAeq_dict[i] = []

            for row in filereader:

                # do other stuff
                # grab info
                time = row[1].split(":")
                hour = int(time[0])

                if hour != current_hour:
                    if current_hour != -1:
                        size = len(current_LAeq_list)
                        current_LAFmax_list.sort()
                        current_LAFmin_list.sort()
                        current_LAeq_list.sort()

                        #LAFmax_dict[current_hour].append(sum(current_LAFmax_list) / len(current_LAFmax_list))
                        #LAFmin_dict[current_hour].append(sum(current_LAFmin_list) / len(current_LAFmin_list))
                        #LAeq_dict[current_hour].append(sum(current_LAeq_list) / len(current_LAeq_list))
                        LAFmax_dict[current_hour].append(current_LAFmax_list[int(size/2)])
                        LAFmin_dict[current_hour].append(current_LAFmin_list[int(size / 2)])
                        LAeq_dict[current_hour].append(current_LAeq_list[int(size / 2)])

                        current_LAFmax_list.clear()
                        current_LAFmin_list.clear()
                        current_LAeq_list.clear()
                        current_hour = hour
                    else:
                        current_hour = hour

                current_LAFmax_list.append(float(row[5]))
                current_LAFmin_list.append(float(row[6]))
                current_LAeq_list.append(float(row[7]))

            for i in range(0, 24):
                max_list = LAFmax_dict[i]
                min_list = LAFmin_dict[i]
                avg_list = LAeq_dict[i]
                filewriter.writerow([i,
                                    sum(max_list)/len(max_list),
                                    sum(min_list)/len(min_list),
                                    sum(avg_list)/len(avg_list)])


if __name__ == '__main__':
    #average_db_per_hour()
    db_per_hour_all_days_stats()
