def longest_word(file):
    data = []
    
    for unit in open(file, encoding="utf-8"):
        data.append(unit.strip())


    for word in data:
        if len(word) > len(data):
            data = word
    print(word)

    
longest_word("words.txt")
