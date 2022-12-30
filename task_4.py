def reversed_words():
    data = []

    for unit in open("words.txt", encoding="utf-8"):
        data.append(unit.strip())
    
    unique_words = set(data)
    words_repeated = set()
    results = []
    
    for word in unique_words:
        reversed_word = word[::-1]
        if reversed_word in words_repeated:
            results.append((word, reversed_word))
        else:
            words_repeated.add(word)

 

    return results
