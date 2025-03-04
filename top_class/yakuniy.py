
import string

def is_pangram(text):
    alphabet = set(string.ascii_lowercase)  # Ingliz alifbosi: {'a', 'b', 'c', ..., 'z'}
    text_set = set(text.lower())  # Matnni kichik harflarga o'tkazamiz va harflar to‘plamini olamiz
    return alphabet.issubset(text_set)  # Barcha harflar borligini tekshiramiz

# Sinov uchun matn
sentence = "The quick brown fox jumps over the lazy ."
print(is_pangram(sentence))  # True (Pangram)
