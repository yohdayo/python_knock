def skip(string):
    #stringを逆順表示
    rev_string = string[0:len(string):1] # [start:stop:step]
    print(rev_string)

if __name__ == '__main__':
    string = "パタトクカシーー"
    skip(string)