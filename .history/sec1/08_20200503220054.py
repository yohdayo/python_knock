def cipher(input_str):
    return ''.join(chr(219 - ord(c)) if c.islower() else c for c in string)
    """
    result = ""
    for c in input_str:
        print(c)
        if c.islower(): #islower()は小文字の判定．英大文字が含まれていない場合、Trueを返す
            result.join(chr(219 - ord(c)))
            print(result)
            #小文字なら変換
        else:
            result.join(c)
            #大文字はそのまま
    
    return result
    """

if __name__ == '__main__':
    input_str = input('Please input: ')
    #print(type(input_str))
    ex = cipher(input_str)
    print(ex)
    ex = cipher(ex)
    print(ex)