def longest_word():
    data = []

    for unit in open("words.txt", encoding="utf-8"):
        data.append(unit.strip())

    the_longest_word = ""
    for word in data:
        if len(word) > len(the_longest_word):
            the_longest_word = word
    return the_longest_word
