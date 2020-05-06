def merge_files(file1, file2, out_file):
    with open(out_file, ‘w’) as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


if __name__ == '__main__':
    file1 = 'col1.txt'
    file2 = 'col2.txt'
    out_file = 'merged.txt'
    merge_files(file1,file2, out_file)
