import sys

def print_lines(file_name, n):
    with open (file_name "r") as file:
        lines = file.readlines()
        print(lines[0:n])

    

if __name__ == '__main__':
    file_name = '../datas/hightemp.txt'
    args = sys.argv
    n = args[1]

    print_lines(file_name, n)