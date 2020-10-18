fruits = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
fruits['apple']='green'
print('The apple is ' +fruits['apple'])
fruits['peach']='pink'
print(fruits)
for fruit_key in fruits:
    print('The ' + fruit_key + ' is ' + fruits[fruit_key])
