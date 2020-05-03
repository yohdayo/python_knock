def make_bigram(str):
    ngram = (str[i:2+i] for i in range(int(len(str))-3))
    return ngram

def get_union(target1, target2):
    print(type(target1))
    u1 = set(target1)
    u2 = set(target2)
    
if __name__ == '__main__':
    str1 = "paraparaparadise"
    str2 = "paragraph"

    bi_str1 = list(make_bigram(str1))
    bi_str2 = list(make_bigram(str2))
    get_union(bi_str1, bi_str2)
    