import nltk, os
os.chdir('C:\\Users\\Nathan\\Documents\\LING 360\\Final Project\\text')
# loop through files in directory
for b in os.listdir(os.getcwd()):
  # initialize part of speech counters to zero
  pos_counts = dict.fromkeys(['ADJ','ADP','ADV','CONJ','DET','NOUN','NUM','PRT','PRON','VERB','.','X'], 0)
  for t in os.listdir(f'C:\\Users\\Nathan\\Documents\\LING 360\\Final Project\\text\\{b}'):
    with open(f'C:\\Users\\Nathan\\Documents\\LING 360\\Final Project\\text\\{b}\\{t}', mode='r', encoding='utf8') as f:
      text = f.read()
      words = nltk.word_tokenize(text)
      tagged = nltk.pos_tag(words, tagset='universal')
      for i in tagged:
        if i[1] == 'ADJ':
          pos_counts['ADJ'] += 1
        elif i[1] == 'ADP':
          pos_counts['ADP'] += 1
        elif i[1] == 'ADV':
          pos_counts['ADV'] += 1
        elif i[1] == 'CONJ':
          pos_counts['CONJ'] += 1
        elif i[1] == 'DET':
          pos_counts['DET'] += 1
        elif i[1] == 'NOUN':
          pos_counts['NOUN'] += 1
        elif i[1] == 'NUM':
          pos_counts['NUM'] += 1
        elif i[1] == 'PRT':
          pos_counts['PRT'] += 1
        elif i[1] == 'PRON':
          pos_counts['PRON'] += 1
        elif i[1] == 'VERB':
          pos_counts['VERB'] += 1
        elif i[1] == '.':
          pos_counts['.'] += 1
        else:
          pos_counts['X'] += 1
  pos_counts = sorted(pos_counts.items(), reverse = True, key = lambda x:x[1])
  print(f'{b} {pos_counts}')