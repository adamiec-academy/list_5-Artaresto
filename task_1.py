def longest_word(file):
    data = []
    
    for unit in open(file, encoding="utf-8"):
        data.append(unit.strip())

    longest_word = ""
    for word in data:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)

longest_word("./listy/lista05/words.txt")
    
