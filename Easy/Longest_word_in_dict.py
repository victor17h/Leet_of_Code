words = ["w","wo","wor","worl","world","as"]


def longest_word(words):
    longest = ''
    for word in words:
        if len(longest)<len(word):
            longest = word
    return longest


print(longest_word(words))