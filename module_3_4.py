def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in other_words:
        k = i.lower()
        if root_word in k or k in root_word:
            same_words.append(i)
        else:
            continue
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel', 'Eme')
print(result1)
print(result2)