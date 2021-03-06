import pandas as pd
import matplotlib.pyplot as plt
import mplleaflet

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


# Parse the initial given txt dataset
def parse_everything():
    my_file = open("data/emissions.txt", "r")
    info = my_file.readlines()

    lat = []
    long = []

    info = info[1:]  # remove the first line, which is just column names
    for i in range(len(info)):
        info[i] = info[i].split(",")
        cleaned_data = []

        # print info[i][3]
        # print info[i][4]
        if info[i][3][0] == '"':
            real_num = int(info[i][3][1:] + info[i][4][:-1])
            cleaned_data.append(real_num)
            cleaned_data.append(info[i][13])
            cleaned_data.append(info[i][16])
            cleaned_data.append(info[i][17])

        else:
            real_num = int(info[i][3])
            cleaned_data.append(real_num)
            cleaned_data.append(info[i][12])
            cleaned_data.append(info[i][15])
            cleaned_data.append(info[i][16])

        info[i] = cleaned_data

        # print info[i]

        if len(cleaned_data[2]) != 0 and len(cleaned_data[3]) != 0 and "/" not in cleaned_data[2] \
                and "/" not in cleaned_data[3]:
                lat.append(float(cleaned_data[2]))
                long.append(float(cleaned_data[3]))

    return lat, long


# ---
# my_info = parse_everything()
#
# plt.hold(True)
#
# plt.plot(my_info[1], my_info[0], "ro")
#
# mplleaflet.show()
# ---

def use():
    return parse_everything()
