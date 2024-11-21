1 # create a dictionary with the three key-value pairs representing a student's information: name, age, grade. print each key-value pair on a new line
student = {'name':'Shakirah','age': 30, 'grade':'A'}
print('name', student['name'])
print("age", student['age'])
print('grade', student['grade'])

2# Write a function that takes a dictionary of people's names and their ages,{Alice, 24, Bob, 19, Charles, 30} and returns a list of names of people who are 21 or older.
def filter_adults(people):
    return [name for name,age in people.items() if age >= 21]
people = {'Alice':24, 'Bob':19, 'Charlie':30}
adults = filter_adults(people)
print(adults )
3# Given a dictionary representing items in a store with their prices,{apple, 0.5, banana, 0.3, orange, o.7}, write a program that takes a list of items bought, [apple, orange, banana, banana], ad calculates the total cost
store = {'apple':0.5,'banana':0.3,'orange':0.7,}
items_bought = ['apple','orange','banana','banana']
total_cost = sum(store[item]for item in items_bought)
print(f'total cost:{total_cost}')

4# write a program that counts the sentence "hello world hello", the output should be{'hello':2,'world':1}
def word_count(sentence):
    words = sentence.split() 
    counts = {}
    for word in words:counts[word]= counts.get(word,0) + 1
    return counts

sentence = 'hello world hello'
counts = word_count(sentence)
print(counts)
