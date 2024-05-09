print('We will find out how much percentage you will need in final year to get 70%')
first =  input('what was your average percentage in first year?')
second = input('what was your average percentage in second year?')
third = input('what was your average percentage in third year?')
required = (70 - (0.2* int(first) + 0.2* int(second) + 0.3* int(third)))/0.3
print('you need to get', required, 'percent in final year to get 70%')
