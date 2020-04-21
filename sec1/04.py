def sprit(string):
    words = string.split(' ')

    result = []
    for word in words:
        result.append(len(word) - word.count(',') - word.count('.'))
        #, . を除いた文字数をresultに格納

    print(result)

if __name__ == '__main__':
    string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    sprit(string)