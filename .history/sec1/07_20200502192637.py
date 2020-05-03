import sys

def print_text():
    args = sys.argv
    x = args[1]
    y = args[2]
    z = args[3]
    print(str(x) + '時の' + y + 'は' + str(z))

if __name__ == '__main__':
    print_text()