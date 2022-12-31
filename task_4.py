def reversed_words():
    data = set()

    for unit in open("listy/lista05/words.txt", encoding="utf-8"):
        data.add(unit.strip())
    

    results = []
    for word in data:
        if word[::-1] in data and word not in results:
            reversed_word = word[::-1]
            results.append((word, reversed_word))
    
    return results


