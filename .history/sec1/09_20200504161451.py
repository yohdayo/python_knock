import random

def typoglycemia(sentence):
    words = sentence.split(" ")
    print(words)

    random = []
    for word in words:
        if len(word) < 4:
            random.append(word)
    print(random)
            
            

    


if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    typoglycemia(sentence)