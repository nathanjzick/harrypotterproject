from textblob import TextBlob
import os

def calculateSentiment(text):
    blob = TextBlob(text)
    score = 0
    for s in blob.sentences:
      score += s.sentiment.polarity
    score = score / len(blob.sentences)
    score = round(score, 4)
    return score

os.chdir('C:\\Users\\Nathan\\Documents\\LING 360\\Final Project\\text')
for b in os.listdir(os.getcwd()):
  # loop through chapters in the book directory
  for c in os.listdir(f'C:\\Users\\Nathan\\Documents\\LING 360\\Final Project\\text\\{b}'):
    with open(f'C:\\Users\\Nathan\\Documents\\LING 360\\Final Project\\text\\{b}\\{c}', mode='r', encoding='utf8') as f, open(f'C:\\Users\\Nathan\\Documents\\LING 360\\Final Project\\charts\\sentiment.csv', mode='a') as csv:
      sentiment = calculateSentiment(f.read())
      csv.write(f'{f.name},{sentiment}\n')
