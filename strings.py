strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for string in strings:
	sentence=sentence+string+' '
print(sentence.rstrip())
print(' '.join(strings))
