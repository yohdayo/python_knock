import test

def save_col(file_name):
    with open(file_name, 'r') as f:
        sp_array = []
        for line in f:
            sp_line = line.split(" ")
            print(sp_line)


if __name__ == '__main__':
    file_name = '../datas/hightemp.txt'
    exchanged = test.tab_to_space(file_name)
    print(exchanged)
    save_col(file_name)