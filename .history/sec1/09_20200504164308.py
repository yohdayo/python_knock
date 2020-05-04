import random

def typoglycemia(sentence):
    words = sentence.split(" ") #半角空白で単語に分ける

    result = []
    for word in words:
        if len(word) < 4:
            result.append(word)
        else:
            s = word[0]
            #s += random.sample(word, len(word[1:-1]))
            s += word[-1]
            result.append(s)

    print(result)
            
if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    typoglycemia(sentence)