def longest_word(file):
    data = []
    
    for unit in open("words.txt", encoding="utf-8"):
        data.append(unit.strip())

    longest_word = ""
    for word in data:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

longest_word("words.txt")
    
