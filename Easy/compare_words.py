word1 = ["ab", "c"]
word2 = ["a", "bc"]


def words(word1,word2):
    return True if "".join(word1) == "".join(word2) else False


print(words(word1,word2))