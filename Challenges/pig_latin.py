#Converts a word into pig latin, needs to be cleaned up
def pig_latin(word):
  word = list(word)
  first_letter = word[0]
  del word[0]
  word.insert(len(word),first_letter)
  word.insert(len(word),'ay')
  print(''.join(word))
  
  #Suggested edits via StackOverflow -------------------
  def pig_latin(word):
    """Coverts to Pig Latin; moves first letter to end, and adds 'ay' to end
    """
    word = list(word)
    first_letter = word[0]
    del word[0]
    word.append(first_letter)
    word.append('ay')
    print(''.join(word))
    
  def pig_latin(word):
    print('%s%say'%(word[1:],word[0]))
  #-----------------------------------------------------
  
