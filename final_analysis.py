import nltk, os
os.chdir('C:\\Users\\Nathan\\Documents\\LING 360\\Final Project\\text')
# loop through books in the text directory
for b in os.listdir(os.getcwd()):
  # initialize part of speech counters to zero
  pos_counts = dict.fromkeys(['ADJ','ADP','ADV','CONJ','DET','NOUN','NUM','PRT','PRON','VERB','.','X'], 0)
  # loop through chapters in the book directory
  for t in os.listdir(f'C:\\Users\\Nathan\\Documents\\LING 360\\Final Project\\text\\{b}'):
    with open(f'C:\\Users\\Nathan\\Documents\\LING 360\\Final Project\\text\\{b}\\{t}', mode='r', encoding='utf8') as f:
      # reads text
      text = f.read()
      # tokenizes text into words
      words = nltk.word_tokenize(text)
      # tags words with universal tagset
      tagged = nltk.pos_tag(words, tagset='universal')
      # big if else chain to increment correct counters for each tagged word
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
  # sorts dictionary to show most frequent part of speech first
  pos_counts = sorted(pos_counts.items(), reverse = True, key = lambda x:x[1])
  print(f'{b} {pos_counts}')