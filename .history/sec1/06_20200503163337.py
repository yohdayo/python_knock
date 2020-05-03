def make_bigram(str):
    #bi-gramを作る
    ngram = (str[i:2+i] for i in range(int(len(str))-3))
    return ngram

def get_union(target1, target2):
    #和集合
    uni = target1 | target2 #u1とu2の和集合
    print("union:",uni)

def get_intersection(target1, target2):
    #積集合
    inter = target1 & target2
    print("intersection:",inter) 


def get_difference(target1,target2):
    #差集合
    dif = target1 -target2
    print("difference:",dif)

if __name__ == '__main__':
    str1 = "paraparaparadise"
    str2 = "paragraph"

    bi_str1 = list(make_bigram(str1))
    bi_str2 = list(make_bigram(str2))

    union_bi_str1 = set(bi_str1) #bi_str1の和集合
    union_bi_str2 = set(bi_str2) #bistr2の和集合

    get_union(union_bi_str1, union_bi_str2)
    get_intersection(union_bi_str1, union_bi_str2)
    get_difference(union_bi_str1, union_bi_str2)
    