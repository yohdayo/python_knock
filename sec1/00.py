def reverse(string):
    #stringを逆順表示
    rev_string = string[::-1] # [start:stop:step]
    print(rev_string)

if __name__ == '__main__':
    string = "stressed"
    reverse(string)