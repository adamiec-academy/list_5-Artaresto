def reversed_words():
    data = []

    for unit in open("words.txt", encoding="utf-8"):
        data.append(unit.strip())
    
    unique_words = set(data)
    backwards_check = {word[::-1] for word in unique_words if word != word[::-1]}
    results = []
    check_set = set()
    
    for word in unique_words:
        if word in words_repeated and word not in check_set:
            reversed_word = word[::-1]
            results.append((word, reversed_word))
            check_set.add(word)
            check_set.add(reversed_word)

    return results
