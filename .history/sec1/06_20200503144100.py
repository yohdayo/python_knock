def make_bigram(str):
    ngram = (str[i:2+i] for i in range(int(len(str))-3))
    return ngram

def get_union(target1, target2):
    #u = target1.append(target2)
    print("")

if __name__ == '__main__':
    str1 = "paraparaparadise"
    str2 = "paragraph"

    bi_str1 = make_bigram(str1)
    bi_str2 = make_bigram(str2)
    make_union(bi_str1, bi_str2)
    print(type(bi_str1))