import sys

def print_text(x,y,z):
    print(str(x) + '時の' + str(y) + 'は' + str(z))

if __name__ == '__main__':
    args = sys.argv
    x = args[1]
    y = args[2]
    z = args[3]
    print_text(x,y,z)