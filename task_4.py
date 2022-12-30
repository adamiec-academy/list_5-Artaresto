def reversed_words():
    data = []

    for unit in open("listy/lista05/words.txt", encoding="utf-8"):
        data.append(unit.strip())
    
    unique_words = set(data)
    words_repeated = set()
    check_set = set()
    results = []
    
    for word in unique_words:
        reversed_word = word[::-1]
        if reversed_word in words_repeated and word not in check_set:
            results.append((word, reversed_word))
            check_set.add(word)
            check_set.add(reversed_word)
        else:
            words_repeated.add(word)

    return results
