from datetime import datetime


# Parse the initial given txt dataset
def parse_everything():
    my_file = open("data/floodingheatmap12m.txt", "r")
    info = my_file.readlines()

    info = info[1:]  # remove the first line, which is just column names
    for i in range(len(info)):
        info[i] = info[i].split("|")
        del info[i][0]  # all weights are 1..?
        del info[i][0]  # don't need latitude
        del info[i][0]  # don't need longitude
        del info[i][2]  # don't need closed date
        del info[i][2]  # don't need due date
        del info[i][2]  # don't need case type, since they are all "FLOODING"
        del info[i][2]  # don't need case number

        info[i][1] = datetime.strptime(info[i][1][:-13], "%Y-%m-%d")
        # print info[i][1][:-13]

    return info


# data: output from parse_everything [address, date]
# time_compare: before, during, after
# start_date: date to compare with
# end_date: only used when time_compare = "during"
def filter_date(data, time_compare, start_date, *end_date):
    ret_data = []

    for item in data:
        if time_compare == "before":
            if item[1] < start_date:
                ret_data.append(item)
        elif time_compare == "during":
            # print start_date
            # print item[1]
            # print end_date
            if start_date <= item[1] <= end_date:
                ret_data.append(item)
        elif time_compare == "after":
            if item[1] > start_date:
                ret_data.append(item)
        else:
            return "ERROR"


def before_flood(data):
    start_date = datetime.strptime("08-17-17", "%m-%d-%y")
    # print start_date

    return filter_date(data, "before", start_date)


def during_flood(data ):
    start_date = datetime.strptime("08-17-17", "%m-%d-%y")
    end_date = datetime.strptime("09-02-17", "%m-%d-%y")

    return filter_date(data, "during", start_date, end_date)


def after_flood(data):
    end_date = datetime.strptime("09-02-17", "%m-%d-%y")

    return filter_date(data, "after", end_date)


# print before_flood(parse_everything())
print parse_everything()