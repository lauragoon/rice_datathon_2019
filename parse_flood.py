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

        info[i][1] = datetime.strptime(info[i][1][:-4], "%Y-%m-%d %H:%M:%S")
        # print info[i][1][:-4]

    return info

# data is output from parse_everything [address, date]
def before_flood(data):
    return

def during_flood():
    return

def after_flood():
    return


print parse_everything()