def merge_files(file1, file2, out_file):
    with open(out_file,'w') as out,open(file1, 'r') as in1, open(file2, 'r') as in2:

        #zipするためにtxtの内容をlistにする
        in1_list = []
        for line1 in in1:
            in1_list.append(line1.replace("\n", "")) #改行文字をなくす
        in2_list = []
        for line2 in in2:
            in2_list.append(line2)
        
        #col1とcol2を結合して格納
        for (prefecture, city) in zip(in1_list, in2_list):
            out_line = (prefecture +"\t"+city)
            out.write(out_line)   

if __name__ == '__main__':
    file1 = 'col1.txt'
    file2 = 'col2.txt'
    out_file = 'merged.txt'
    merge_files(file1, file2, out_file)
