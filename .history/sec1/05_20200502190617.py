import sys

def make_ngram(sequence, n):
    ngram = (sequence[i:i+n] for i in range(int(len(sequence))-n+1))
    return ngram

if __name__ == '__main__':
    args = sys.argv
    sequence = args[1]
    n = int(args[2])
    result = make_ngram(sequence, n)
    print("Letter_n-gram:",end="")
    print(list(result))
    print("Word_n-gram:",end="")
    sup_sequence = sequence.split(' ')
    result = make_ngram(sup_sequence, n)
    print(list(result))