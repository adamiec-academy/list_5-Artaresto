def reversed_words():
    data = set()

    for unit in open("words.txt", encoding="utf-8"):
        data.add(unit.strip())
    
    results = []
    
    for word in data:
        reversed_word = word[::-1]
        if reversed_word in data and  reversed_word != word:
            results.append(tuple(sorted((word, reversed_word))))
    
    results = list(set(results))    
    results.sort()
    return results

