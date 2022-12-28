def longest_word(file):
    data = []
    
    for unit in open(file, encoding="utf-8"):
        data.append(unit.strip())


    sorted(data, key = len)
    print(data[-1])
    
longest_word("words.txt")
