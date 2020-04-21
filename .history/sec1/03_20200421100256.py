def sprit(string):
    words = string.split(' ')
    print(words)
    result = []
    for word in words:
        result.append(len(word) - word.count(',') - word.count('.'))

    print(result)

if __name__ == '__main__':
    string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    sprit(string)