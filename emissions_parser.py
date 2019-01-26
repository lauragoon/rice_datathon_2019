# Parse the initial given txt dataset
def parse_everything():
    my_file = open("data/emissions.txt", "r")
    info = my_file.readlines()

    info = info[1:]  # remove the first line, which is just column names
    for i in range(len(info)):
        info[i] = info[i].split(",")
        cleaned_data = []
        cleaned_data.append(info[i][3])
        cleaned_data.append(info[i][4])
        cleaned_data.append(info[i][13])
        cleaned_data.append(info[i][16])
        cleaned_data.append(info[i][17])
        info[i] = cleaned_data

        # info[i][1] = datetime.strptime(info[i][1][:-13], "%Y-%m-%d")
        # print info[i][1][:-13]

    return info


print parse_everything()