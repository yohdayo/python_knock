def cipher(input_str):
    result = ""
    for c in input_str:
        if c.islower(): #islower()は小文字の判定．英大文字が含まれていない場合、Trueを返す
            result.join(chr(219 - ord(c)))
        else:
            result.join(c)
    
    return result
        
    



if __name__ == '__main__':
    input_str = input('Please input: ')
    print(type(input_str))
    ex = cipher(input_str)
    print(ex)
    ex = cipher(ex)
    print(ex)