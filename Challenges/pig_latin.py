#Converts a word into pig latin, needs to be cleaned up
def pig_latin(word):
  word = list(word)
  first_letter = word[0]
  del word[0]
  word.insert(len(word),first_letter)
  word.insert(len(word),'ay')
  print(''.join(word))
