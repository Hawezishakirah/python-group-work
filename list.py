1 #create a list of 5 fruits and print each  new line using a for loop.
fruit_names = ['mangoes','pears','pawpaws','apples','oranges' ]
for fruit in fruit_names:
    print(fruit)

2. # wtite a function that takes a list of numbers and returns a new list with each number squared . eg:[1.2.3]
#should become [1,4,9].
def list_of_numbers (numbers):
  return [number ** 2 for number in numbers]
numbers=[1,2,3]
squared = list_of_numbers(numbers)
print(squared)
3.#write a python program that takes two lists, list1 =[1,2,3]and list2 =[4,5,6]and combines them into a single list
#combined = [1,4,2,5,3,6]
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)
4.#given a list of numbers [3,1,4,1,5,9,2].write a program to find and print the two largest nimbers in the list without using 
#the max().
numbers = [3,1,4,1,5,9,2]
largest = -float('inf')
second_largest = -float('inf')

for num in numbers:
   if num > largest:
      second_largest = largest
      largest = num
   elif num > second_largest and num != largest:second_largest = num
print(f'The two largest numbers are {largest} and {second_largest}')

