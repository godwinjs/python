def word_search(doc_list, keyword):
    indices = { word: [] for word in keyword }

    print(indices)

    for i, doc in enumerate(doc_list):
        word = doc.split()
        formated_arr = [ word.lower().rstrip(',?!.') for word in word ]

        for key_w in keyword:
            # indices.append(i)
            if key_w in formated_arr:
                indices[key_w].append(i)
    print(indices)
word_search(['They Learn Python Challenge Casino and car', 'They bought a car, and a horse', 'Casinoville?'], ["car", "casino"])
# word_search(["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"], "casino")