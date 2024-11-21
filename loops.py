1. #write a program that prints all even nos btn 1 and 20 using a for loop
def even_numbers():
  for num in range(2, 22, 2):
    print(num)

even_numbers()  

2. # use a while loop to ask the user to input a number until they provide a no greater than 10
while True:
  num = int(input("Enter a number greater than 10:"))
  if num > 10:
    print(f'You entered {num}.')
    break

3  #write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops
for  a in range(1, 6): 
  for b in range(1, 11):
    print(f'{a} * {b} = {a * b}')
print()
4 #given a list of integers, [4,7,2,9,12,15], write a program using a for loop to find the sum of all odd numbers and print the result
numbers = [ 7,  9, 15]
total = sum(numbers)
print(f'sum of all odd numbers {total}')
