def make_bigram(string):
    ngram = (sequence[0:2+i] for i in range(int(len(sequence))-3))
    return ngram

if __name__ == '__main__':
    str1 = "paraparaparadise"
    str2 = "paragraph"