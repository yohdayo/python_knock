def cipher(input_str):
    return(.join(chr(219 - ord(input_str)) if c.islower() else c for c in string))
    



if __name__ == '__main__':
    input_str = input('Please input: ')
    ex = cipher(input_str)
    print(ex)