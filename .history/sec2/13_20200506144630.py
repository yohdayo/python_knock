def merge_files(file1, file2, out_file):
    with open(out_file,'w') as out,open(file1, 'r') as in1, open(file2, 'r') as in2:
        in1_list = []
        in2_list = []

        for line1 in in1:
            in1_list.append(line1.replace("\n", ""))
        for line2 in in2:
            in2_list.append(line2)
        
        print(in2_list)
        """
        for (prefecture, city) in zip(in1, in2):
            out_line = (prefecture +"\t"+city)
            print(out_line)
            out.write(out_line)
        """    

if __name__ == '__main__':
    file1 = 'col1.txt'
    file2 = 'col2.txt'
    out_file = 'merged.txt'
    merge_files(file1, file2, out_file)
