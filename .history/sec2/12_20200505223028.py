def tab_to_space(file_name):
    with open(file_name, 'r') as f:
        result = []
        for line in f:
            ex =line.replace("\t", " ")
            result.append(ex)

    return result

def save_col(lines):
        sp_array = []
        for line in f:
            sp_line = line.split(" ")
            print(sp_line)


if __name__ == '__main__':
    file_name = '../datas/hightemp.txt'
    exchanged = tab_to_space(file_name)
    print(exchanged)
    save_col(exchanged)