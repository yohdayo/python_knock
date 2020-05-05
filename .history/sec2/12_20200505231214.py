def tab_to_space(file_name):
    with open(file_name, 'r') as f:
        result = []
        for line in f:
            ex =line.replace("\t", " ")
            result.append(ex)

    return result

def save_col1(lines, outfile):
    with open(outfile, 'w') as f:
        for line in lines:
            sp_line = line.split(" ")
            print(type(sp_line[0]))
            #f.writelines(sp_line[0])
    
if __name__ == '__main__':
    file_name = '../datas/hightemp.txt'
    exchanged = tab_to_space(file_name)
    out_file1 = '.col1.txt'
    out_file2 = '.col2.txt'
    save_col1(exchanged,out_file1)
    #save_col(exchanged,out_file2)
