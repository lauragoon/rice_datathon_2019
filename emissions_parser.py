# Parse the initial given txt dataset
def parse_everything():
    my_file = open("data/emissions.txt", "r")
    info = my_file.readlines()

    info = info[1:]  # remove the first line, which is just column names
    for i in range(len(info)):
        info[i] = info[i].split(",")
        cleaned_data = []

        print info[i][3]
        print info[i][4]
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

        # info[i][1] = datetime.strptime(info[i][1][:-13], "%Y-%m-%d")
        # print info[i][1][:-13]

    return info


print parse_everything()