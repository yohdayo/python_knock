def merge_files(file1, file2, out_file):
    with open(out_file,'w') as out,open(file1, 'r') as in1, open(file2, 'w') as in2:
        for (prefecture, city) in zip(in1, in2):
            input = (prefecture +"\t"+city)
            out.write(input)


if __name__ == '__main__':
    file1 = 'col1.txt'
    file2 = 'col2.txt'

    out_file = 'merged.txt'
    merge_files(file1,file2, out_file)
