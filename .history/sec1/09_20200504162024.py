import random

def typoglycemia(sentence):
    words = sentence.split(" ")
    print(words)

    result = []
    for word in words:
        if len(word) < 4:
            result.append(word)
        else:
            s = random.sample(word)
            result.append(s)

    print(random)
            
if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    typoglycemia(sentence)