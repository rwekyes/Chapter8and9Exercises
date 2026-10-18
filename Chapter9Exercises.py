# Exercise 9.15.2

def is_anagram(word1, word2):
    return sorted(list(word1.lower())) == sorted(list(word2.lower()))

#print(is_anagram("SANTA", "SATAN"))

count = 0
for line in open('words.txt'):
    word = line.strip()
    if is_anagram(word, "takes") and word != "takes":
        count += 1

print(f"takes has {count} anagrams in the word list")

# Exercise 9.15.3

def reverse_word(word):
    return ''.join(reversed(word))

def is_palindrome(word):
    if word == reverse_word(word):
        return True
    return False

count = 0

for line in open('words.txt'):
    word = line.strip()
    if len(word) >= 7 and is_palindrome(word):
        print(word)
        count += 1

print(f"There are {count} palindromes with more than 7 letters in the word list")

# Exercise 9.15.4

def reverse_sentence(sentence):
    return ' '.join(reversed(sentence.split())).capitalize()

#print(reverse_sentence("Smoke on the water"))

# Exercise 9.15.5

def total_length(list_of_strings):
    count = 0
    for word in list_of_strings:
        count += len(word)
    return count

word_list = []

for line in open("words.txt"):
    word = line.strip()
    word_list.append(word)

print(f"There are {total_length(word_list)} characters in the word list")