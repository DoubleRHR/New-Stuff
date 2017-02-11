#Reverses a given thing
#Needs to be more elegant, but it'll do
def rvrs():
  str_input = input("Enter a string: ")
  str_input = list(str_input[::-1])
  str_input = ''.join(str_input)
  print(str_input)
