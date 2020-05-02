import sys

def sprit(string):
    words = string.split(' ')

def make_ngram(sequence, n):
    print("Letter_n-gram:",end="")
    ngram = (sequence[i:i+n] for i in range(int(len(sequence))-n+1))
    print(list(ngram))
    print("Word_n-gram:",end="")

if __name__ == '__main__':
    args = sys.argv
    sequence = args[1]
    n = int(args[2])
    make_ngram(sequence, n)
