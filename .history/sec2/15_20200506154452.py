import sys

def print_min_lines(file_name, n):
    with open (file_name,"r") as file:
        lines = file.readlines()
        for line in lines[-n:]:
            print(line)

if __name__ == '__main__':
    file_name = '../datas/hightemp.txt'
    args = sys.argv
    n = int(args[1])

    print_min_lines(file_name, n)