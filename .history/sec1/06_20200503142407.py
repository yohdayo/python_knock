def make_bigram(str):
    ngram = (str[i:2+i] for i in range(int(len(str))-3))
    return ngram

def make_union(target1, target2):
    u = target1
    u.append(target2)
    print(set(u))

if __name__ == '__main__':
    str1 = "paraparaparadise"
    str2 = "paragraph"

    bi_str1 = make_bigram(str1)
    bi_str2 = make_bigram(str2)
    make_union(str1, str2)