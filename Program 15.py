import string


def get_letter_frequencies(ciphertext):
    frequencies = {letter: 0 for letter in string.ascii_lowercase}
    total_letters = 0

    for letter in ciphertext:
        if letter.isalpha():
            frequencies[letter.lower()] += 1
            total_letters += 1

    for letter in frequencies:
        frequencies[letter] /= total_letters

    return frequencies


def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            is_upper = letter.isupper()
            letter = letter.lower()
            decrypted_letter = chr((ord(letter) - ord('a') - key) % 26 + ord('a'))
            if is_upper:
                decrypted_letter = decrypted_letter.upper()
            plaintext += decrypted_letter
        else:
            plaintext += letter
    return plaintext


def letter_frequency_attack(ciphertext, top_k=10):
    frequencies = get_letter_frequencies(ciphertext)
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    possible_plaintexts = []

    for i in range(26):
        key = i
        plaintext = decrypt(ciphertext, key)
        score = 0
        for j, freq in enumerate(sorted_frequencies):
            score += abs(ord(freq[0]) - ord(plaintext[j].lower()))
        possible_plaintexts.append((score, plaintext))

    possible_plaintexts.sort(key=lambda x: x[0])
    return possible_plaintexts[:top_k]



ciphertext = "Jxu gwcujp xqq gr ejtkzrwp gz xwzpvk. T jgzp qttg fqwq cu yjcv."  # Additive cipher encrypted text
top_k = 10

results = letter_frequency_attack(ciphertext, top_k)

print(f"Top {top_k} possible plaintexts:")
for i, result in enumerate(results, 1):
    score, plaintext = result
    print(f"{i}. Plaintext: {plaintext}, Score: {score}")
