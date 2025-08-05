"""
CP1404/CP5632 Practical
Word Occurrences
"""

text = input("Text: ")
words = text.split()

word_to_count = {}
for word in words:
    word = word.lower()
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

# Sort words alphabetically
sorted_words = sorted(word_to_count.keys())

# Find the longest word for formatting
max_word_length = max(len(word) for word in sorted_words)

# Print results, aligned
for word in sorted_words:
    print(f"{word:{max_word_length}} : {word_to_count[word]}")