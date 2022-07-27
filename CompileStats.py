import csv

# global vars -- change in main()
target_csv = ""
dest_csv = ""


def LAeq_per_30_minutes():
    with open(target_csv, 'r') as readfile:
        filereader = csv.reader(readfile)
        with open(dest_csv, 'w', newline='') as writefile:
            filewriter = csv.writer(writefile)

            filewriter.writerow(["Hour", "LAeq"])  # column headers

            current_30_min_num = 0
            current_30_min_LAeq_list = []
            sec_count = 0

            for row in filereader:
                if filereader.line_num <= 2:
                    continue

                sec_count += 1

                if sec_count > (30 * 60):
                    filewriter.writerow([(current_30_min_num * 0.5),
                                         (sum(current_30_min_LAeq_list) / len(current_30_min_LAeq_list))])
                    current_30_min_num += 1
                    sec_count = 0

                current_30_min_LAeq_list.append(float(row[7]))


# TODO: comment stuff lol
def compile_graph_nums():
    with open(target_csv, 'r') as readfile:
        filereader = csv.reader(readfile)
        with open(dest_csv, 'w', newline='') as writefile:
            filewriter = csv.writer(writefile)

            filewriter.writerow(["Hour of the Day", "LAeq", "LAF_max", "LAF_min"])  # column headers

            LAF_max_dict = {}
            LAF_min_dict = {}
            LAeq_dict = {}
            current_hour = -1
            current_LAF_max_list = []
            current_LAF_min_list = []
            current_LAeq_list = []

            for i in range(0, 24):
                LAF_max_dict[i] = []
                LAF_min_dict[i] = []
                LAeq_dict[i] = []

            for row in filereader:
                if filereader.line_num <= 2:
                    continue

                # grab info
                time = row[1].split(":")
                hour = int(time[0])

                if hour != current_hour:
                    if current_hour != -1:
                        size = len(current_LAeq_list)

                        for i in range(size):
                            LAF_max_dict[current_hour].append(current_LAF_max_list[i])
                            LAF_min_dict[current_hour].append(current_LAF_min_list[i])
                            LAeq_dict[current_hour].append(current_LAeq_list[i])

                        current_LAF_max_list.clear()
                        current_LAF_min_list.clear()
                        current_LAeq_list.clear()
                        current_hour = hour
                    else:
                        current_hour = hour

                current_LAF_max_list.append(float(row[5]))
                current_LAF_min_list.append(float(row[6]))
                current_LAeq_list.append(float(row[7]))

            for i in range(0, 24):
                max_list = LAF_max_dict[i]
                min_list = LAF_min_dict[i]
                avg_list = LAeq_dict[i]
                filewriter.writerow([i,
                                     sum(avg_list) / len(avg_list),
                                     sum(max_list) / len(max_list),
                                     sum(min_list) / len(min_list)])


# computes following stats:
#   - LAeq, average LAF_max, average LAF_min overall
#   - same but for daytime vs. nighttime
def compile_all_stats():
    with open(target_csv, 'r') as readfile:
        filereader = csv.reader(readfile)
        with open(dest_csv, 'w', newline='') as writefile:
            filewriter = csv.writer(writefile)

            filewriter.writerow(["", "Overall", "Daytime", "Nighttime"])  # column headers

            # day = [7am, 7pm), night = [7pm, 7am)
            day_LAF_max_list = []
            day_LAF_min_list = []
            day_LAeq_dt_list = []
            night_LAF_max_list = []
            night_LAF_min_list = []
            night_LAeq_dt_list = []

            for row in filereader:
                if filereader.line_num <= 2:
                    continue

                # grab info
                time = row[1].split(":")
                hour = int(time[0])

                if 7 <= hour < 19:
                    day_LAF_max_list.append(float(row[5]))
                    day_LAF_min_list.append(float(row[6]))
                    day_LAeq_dt_list.append(float(row[7]))
                else:
                    night_LAF_max_list.append(float(row[5]))
                    night_LAF_min_list.append(float(row[6]))
                    night_LAeq_dt_list.append(float(row[7]))

            # compute and write stats
            LAeq_overall = (sum(day_LAeq_dt_list) + sum(night_LAeq_dt_list)) / (len(day_LAeq_dt_list) + len(night_LAeq_dt_list))
            LAeq_daytime = (sum(day_LAeq_dt_list) / len(day_LAeq_dt_list))
            LAeq_nighttime = (sum(night_LAeq_dt_list) / len(night_LAeq_dt_list))
            filewriter.writerow(["LAeq", LAeq_overall, LAeq_daytime, LAeq_nighttime])

            LAF_max_overall = (sum(day_LAF_max_list) + sum(night_LAF_max_list)) / (len(day_LAF_max_list) + len(night_LAF_max_list))
            LAF_max_daytime = (sum(day_LAF_max_list) / len(day_LAF_max_list))
            LAF_max_nighttime = (sum(night_LAF_max_list) / len(night_LAF_max_list))
            filewriter.writerow(["LAF_max",LAF_max_overall, LAF_max_daytime, LAF_max_nighttime])

            LAF_min_overall = (sum(day_LAF_min_list) + sum(night_LAF_min_list)) / (len(day_LAF_min_list) + len(night_LAF_min_list))
            LAF_min_daytime = (sum(day_LAF_min_list) / len(day_LAF_min_list))
            LAF_min_nighttime = (sum(night_LAF_min_list) / len(night_LAF_min_list))
            filewriter.writerow(["LAF_min", LAF_min_overall, LAF_min_daytime, LAF_min_nighttime])


# change names of CSV files as needed
# run each method one at a time, then paste them into a master doc for the given location
if __name__ == '__main__':
    target_csv = "<name>.csv"   # .csv
    dest_csv = "<name>.csv"     # .csv
    LAeq_per_30_minutes()
    #compile_graph_nums()
    #compile_all_stats()
