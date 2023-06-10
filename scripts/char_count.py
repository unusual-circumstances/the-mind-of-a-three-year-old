# a to get info about my docs

count_char = open('../docs/developer-log.md')
char = count_char.read()
char_count = len(char)
print('the chosen file has', char, 'characters')

count_word = open('../docs/developer-log.md')
word = count_word.read()
print(len(word))

# WIP!!