def analyz(file):
    with open(file, "r", encoding="utf-8") as file:
        text = file.read()
    words = text.split()
    sentences = text.split('.')
    word_frequency = {}
    for word in words:
        word = word.strip(",.;:!?").lower()
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    sentence_lengths = [len(sentence.split()) for sentence in sentences]
    print("Статистика текста:")
    print(f"Количество слов: {len(words)}")
    print(f"Количество предложений: {len(sentences)}")
    print("Частота слов:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")
    print("Длина предложений (в словах):")
    for length in sentence_lengths:
        print(length)
    with open("statistics.txt", "w", encoding="utf-8") as stats_file:
        stats_file.write("Статистика текста:\n")
        stats_file.write(f"Количество слов: {len(words)}\n")
        stats_file.write(f"Количество предложений: {len(sentences)}\n")
        stats_file.write("Частота слов:\n")
        for word, frequency in word_frequency.items():
            stats_file.write(f"{word}: {frequency}\n")
        stats_file.write("Длина предложений (в словах):\n")
        for length in sentence_lengths:
            stats_file.write(f"{length}\n")
analyz("data.txt")
