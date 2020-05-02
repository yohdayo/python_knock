import sys

def sprit(string):
    words = string.split(' ')

def make_ngram(sequence, n):
    print("Letter_n-gram:",end="")
    print("Word_n-gram:",end="")
if __name__ == '__main__':
    args = sys.argv
    sequence = args[1]
    n = args[2]
    make_ngram(sequence, n)
