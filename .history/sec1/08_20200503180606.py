def cipher(input_str):
    return("".join(chr(219 - ord(c)) if c.islower() else c for c in input_str))
    
#文字列に英大文字が含まれていない場合、Trueを返すメソッド


if __name__ == '__main__':
    input_str = input('Please input: ')
    ex = cipher(input_str)
    print(ex)
    ex = cipher(input_str)
    print(ex)