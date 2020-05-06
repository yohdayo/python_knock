import sys

def count_line(file_name):
    with open(file_name, 'r') as f:
        sum = 0
        for i in f:
            sum += 1
    
        return sum

def file_separate(file_name, num_of_file_len, n):
    

if __name__ == '__main__':
    file_name = '../datas/hightemp.txt'
    args = sys.argv
    n = int(args[1])
    num_of_file_len = count_line(file_name)
    print(num_of_file_len)
    file_separate(file_name, num_of_file_len, n)
