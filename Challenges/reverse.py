#Reverses a given thing  
#The new and improved version!
def reverse(thing):
  """Reverses a word (ints do NOT work!)
  """
  thing = list(thing[::-1])
  print(''.join(thing)
        
#The original ugly version
def rvrs():
  str_input = input("Enter a string: ")
  str_input = list(str_input[::-1])
  str_input = ''.join(str_input)
  print(str_input)

