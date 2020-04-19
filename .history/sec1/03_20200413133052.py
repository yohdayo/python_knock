def mix(string1, string2):
    for i in range(len(string1)):
        print(string1[i] + string2[i],end = "")
    print()

if __name__ == '__main__':
    string1 = "パトカー"
    string２ = "タクシー"
    mix(string1, string2)