import sys

def make_ngram(sequence, n):
    ngram = (sequence[i:i+n] for i in range(int(len(sequence))-n+1))
    return ngram

if __name__ == '__main__':
    args = sys.argv
    sequence = args[1]
    n = int(args[2])
    #第一引数が対象の文，第二引数はn-gramのn

    result = make_ngram(sequence, n)
    print("Letter_n-gram:",end="")
    print(list(result))
    #文字n-gram

    print("Word_n-gram:",end="")
    sup_sequence = sequence.split(' ')#空白でsplit
    result = make_ngram(sup_sequence, n)
    print(list(result))
    #単語ngram