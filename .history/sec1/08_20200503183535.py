def cipher(input_str):
    result = []
    for c in input_str:
        if c.islower(): 
            result.join(chr(219 - ord(c)))
        else:
            result.join(c)
    return result
        
    
#文字列に英大文字が含まれていない場合、Trueを返すメソッド


if __name__ == '__main__':
    input_str = input('Please input: ')
    ex = cipher(input_str)
    print(ex)
    ex = cipher(ex)
    print(ex)