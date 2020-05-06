import sys

def print_lines(file_name, n):
    with open (file_name,"r") as file:
        lines = file.readlines()
        for i in n
            print(lines[i])

if __name__ == '__main__':
    file_name = '../datas/hightemp.txt'
    args = sys.argv
    n = int(args[1])

    print_lines(file_name, n)