def count_line(file_name):
    with open(file_name, 'r') as f:
        sum = 0
        for line in f:
            sum += 1
    
        return sum
    

if __name__ == '__main__':
    file_name = '../datas/hightemp.txt'

    line_num = count_line(file_name)

    print('line: {}'.format(line_num))
