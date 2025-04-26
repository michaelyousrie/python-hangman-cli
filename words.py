import json
import random

def load_words_from_json(file_path='words.json'):
    with open(file_path, 'r') as file:
        words_list = json.load(file)
    #endwith
    return words_list
#enddef

def get_random_word():
    return random.choice(load_words_from_json())
#enddef

def get_all_words():
    return load_words_from_json()
#enddef

def main():
    print("This should be used as a module. The most useful methods are get_all_words and get_random_word")
#enddef


if __name__ == '__main__':
    main()
#endif