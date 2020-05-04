def tab_to_space(file_name):
    with open(file_name, 'r') as f:
        result = []
        for line in f:
            ex =line.replace("\t", " ")
            result.append(ex)

    return result
    

if __name__ == '__main__':
    file_name = '../datas/hightemp.txt'

    exchanged = tab_to_space(file_name)
    for el in exchanged:
        print(el, end = '')
