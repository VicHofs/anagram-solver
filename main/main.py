from itertools import permutations
string = input('Enter anagram:')
print('-registering permutations...')
with open('anagrams.txt', 'w') as f:
    for inst in permutations(string):
        comp = ''
        comp = comp.join(inst)
        f.write(comp)
        f.write('\n')
    f.close()
print('-done!')
word_length = len(string)
lang = input('-choose a language for analysis:\n\t-English..........en\n\t-Portuguese........pt\n')
if lang == 'en':
    dictionary = open('dict(EN-UK).txt', 'r', encoding='utf-8')
if lang == 'pt':
    dictionary = open('dict(PT-BR).txt', 'r', encoding='utf-8')
anagrams = open('anagrams.txt', 'r', encoding='utf-8')
match = ''
while match == '':
    for i in dictionary:
        dict_entry = i[:-1].lower()
        print(f'-scanning: {dict_entry}')
        if len(dict_entry) != word_length:
            continue
        else:
            possible_match = True
            for j in dict_entry:
                if j not in string:
                    possible_match = False
                    break
            if possible_match:
                for k in string:
                    if not k in dict_entry:
                        possible_match = False
                        break
            if possible_match:
                for x in anagrams:
                    anagram = x[:-1]
                    print(f'-trying: {anagram}')
                    if anagram == dict_entry:
                        match = f'-MATCH FOUND: \n{dict_entry}'
                        break
                anagrams.seek(0)
            if match != '':
                break
    if match == '':
        match = '-NO MATCH-'
dictionary.close()
anagrams.close()

print('\n'* 20)    
print(match)
