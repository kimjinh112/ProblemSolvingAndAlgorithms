list_fruit = ['apple', 'banana', 'tomato']
list_animal = ['bear', 'elephant', 'monkey']
list_instrumental = ['guitar', 'piano', 'harmony']


def len_word(wordlist):
    count = 0
    for word in wordlist:
        count += len(word)
    return count

#print("단어 길이의 합은 ", len_word(list_fruit), "입니다.")

        
def len_word_map(wordlist):
    a = list(map(len, wordlist))
    return sum(a)

print("단어 길이의 합은 ", len_word_map(list_fruit), "입니다.")
