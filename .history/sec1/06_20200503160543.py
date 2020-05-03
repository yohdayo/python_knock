def make_bigram(str):
    ngram = (str[i:2+i] for i in range(int(len(str))-3))
    return ngram

def get_union(target1, target2):
    u1 = set(target1) #bi_str1の和集合
    print(u1)
    u2 = set(target2) #bistr2の和集合
    print(u2)
    u = u1 | u2
    print(u)
if __name__ == '__main__':
    str1 = "paraparaparadise"
    str2 = "paragraph"

    bi_str1 = list(make_bigram(str1))
    bi_str2 = list(make_bigram(str2))
    print(bi_str1)
    print(bi_str2)
    get_union(bi_str1, bi_str2)
    