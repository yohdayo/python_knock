def tab_to_space(file_name):
    with open(file_name, 'r') as f:
       for line in f:
            exchange = line.replace("\t", " ")

       return exchange
    

if __name__ == '__main__':
    file_name = '../datas/hightemp.txt'

    exchanged = tab_to_space(file_name)
    for el in exchange:
        print(el, end = '')

    print(exchanged)