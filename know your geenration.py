age = int(input('enter your age: '))
dob = int(2024 - age)
if dob > 1886 and dob < 1900:
  print('you are form the lost generation. Sorry for the wars')
elif dob > 1901 and dob < 1927:
  print('you are from the greatest generation')
elif dob > 1928 and dob < 1945:
  print('you are from the silent generation')
elif dob > 1945 and dob < 1964:
  print('you are annoying boomer')
elif dob > 1964 and dob < 1980:
  print('you are gen x')
elif dob > 1980 and dob < 1996:
  print('you are a millenial')
elif dob > 1996 and dob < 2012:
  print('oh genZ huh!')
else:
  print('you are from gen alpha')
