def skip(string):
    #stringを逆順表示
    skip_string = string[0:len(string):2] # [start:stop:step]
    print(skip_string)

if __name__ == '__main__':
    string = "パタトクカシーー"
    skip(string)