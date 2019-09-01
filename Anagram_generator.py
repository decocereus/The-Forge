def get_words_in_dict(fname):
    words = {}
    with open(fname) as f:
        for word in f:
            word = word.strip()
            words[word] = words.get(word,0) + 1
    return words

def init_anagram_dict(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(list(word)))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    return anagram_dict

def find_anagram(word, anagram_dict):
    key = ''.join(sorted(list(word)))
    if key in anagram_dict:
        return set(anagram_dict[key]).difference(set([word]))
    return set([])


filename = 'Word_Well.txt'
word_dict = get_words_in_dict(filename)
anagram_dict = init_anagram_dict(word_dict.keys())
myKey = input('Enter: ')
print('The anagrams of',myKey,'are',find_anagram(myKey,anagram_dict))
