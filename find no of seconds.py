ans = input('do you want to find out number of seconds in a yeat (y/n) ?')
if ans == 'y':
  lyear = input('is it a leap year (y/n) ?')
  if lyear == 'y':
    print(' there are ', 366*24*60*60 ,' seconds in a year')
  else:
    print('there are ',365*24*60*60,' seconds in a year')
else:
  print('bad that you dont want to know the number of seconds in a year')
