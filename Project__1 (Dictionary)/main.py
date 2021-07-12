import json
from difflib import get_close_matches

data = json.load(open('data.json'))
word = input('Enter a Word: ').lower()

while True:    
    matched_words = get_close_matches(word, data.keys(), 3, cutoff=0.7)

    if word in data:
        for item in data[word]:
            print(item)
        break
    elif len(matched_words) > 0:
        matched_word = matched_words[0]
        user_choice = input(f'Did you mean {matched_word} instead of {word}? (y/n): ')
        
        if user_choice == 'y':
            word = matched_word
            continue
        elif user_choice == 'n':
            print('The word does not exist. Please double check it.')
            break
        else:
            continue
    else:
        print('The word does not exist. Please double check it.')
        break